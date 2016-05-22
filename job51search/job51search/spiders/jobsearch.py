import scrapy
import time
import os
from selenium import webdriver
from scrapy.selector import Selector
from job51search.items import Job51SearchItem


class jobsearch(scrapy.Spider):
    name = "job"
    allowed_domain = ["51job.com"]
    start_urls = [
                  "http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=030200%2C00&funtype=0000&industrytype=00&keyword=python"
                  ]
    def parse(self, response):
        print response.xpath('//div').extract()
        for sel in response.xpath('//div[@class="el"]/p'):
            
            title = sel.xpath('span/a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            print title, link, desc
            print ' '

class jobsearch2(scrapy.Spider):
    name = "job2"
    allowed_domain = ["search.51job.com"]
    start_urls = [
                  "http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=030200%2C00&funtype=0000&industrytype=00&keyword=python"
                  ]
    
    
    def parse(self, response):
        # use any browser you wish
        fp = webdriver.FirefoxProfile(os.path.expanduser('~/Library/Application Support/Firefox/Profiles/0hn8nym4.default/'))
        fp.set_preference("javascript.enabled",False)
        self.browser = webdriver.Firefox(firefox_profile=fp)

        self.browser.get(response.url)
        # let JavaScript Load
        time.sleep(3)
        
        # scrape dynamically generated HTML
        
        hxs = Selector(text=self.browser.page_source)
        for sel in  hxs.xpath('//div[@class="dw_table"]/div[@class="el"]'):
            #must create multiple items corresponding to every new scrapy request
            item = Job51SearchItem()

            item['jobname'] = ''.join(sel.xpath('p[@class="t1 "]/span/a/text()').extract()).strip()
            item['company'] = sel.xpath('span[@class="t2"]/a/text()').extract()
            item['location'] = sel.xpath('span[@class="t3"]/text()').extract()
            item['salary'] = sel.xpath('span[@class="t4"]/text()').extract()
            item['jobdescriptionlink'] = sel.xpath('p[@class="t1 "]/span/a/@href').extract()
            link = item['jobdescriptionlink'][0]
            request = scrapy.Request(link, callback=self.parse_jobdescription)
            request.meta['item'] = item
            yield request
        
        
        self.browser.close()

    def parse_jobdescription(self, response):
        item = response.meta['item']
        content = []
        for text in response.xpath('//div[@class="bmsg job_msg inbox"]//text()').extract():
            content.append(text.strip())
        
        item['jobdescription'] = ''.join(content).strip()
        return item