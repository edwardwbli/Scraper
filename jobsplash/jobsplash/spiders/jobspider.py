# -*- coding: utf-8 -*-
#Usage:
#scrapy crawl 51job -a qk='scrapy' ja='030200' kwt='2' -o item.csv
#qk for search keyword in 51Job,default is python
#ja for job area, default is guangzhou,
#kwt for keyword type, default is 2 for full text, 1 is for companys search
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy_splash import SplashRequest
from jobsplash.items import Job51SearchItem


class Jobsearch(scrapy.Spider):
    name = "51job"
    allowed_domains = ["51job.com"]
    # http_user = 'splash-user'
    # http_pass = 'splash-password'
    #def start_request(self):
    #    for link in self.start_urls:
    #        yield SplashRequest(link,callback=sel.parse)
    def __init__(self,qk='python',ja='030200',kwt='2'):

        self.start_urls = ["http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea="+ja+"&funtype=0000&industrytype=00&keyword="+qk+"&keywordtype="+kwt+"&lang=c&stype=2&postchannel=0000&fromType=1&confirmdate=9"]
       
   
    def parse(self, response):
        item_count = 0

        joblist =  response.xpath('//div[@class="dw_table"]/div[@class="el"]')
        for jobitem in joblist:
            #must create multiple items corresponding to every new scrapy request
            #if just create single item outside for loop
            #this item will overide until the end of the jobrequest list
            #yield to be a generator with same item reference,
            #
            item = Job51SearchItem()
            jobid = item_count
            item['jobid'] = jobid
            item_count += 1
            
            jobnames  = jobitem.xpath('p/span/a/@title').extract()
            companys  = jobitem.xpath('span[@class="t2"]/a/text()').extract()
            salarys   = jobitem.xpath('span[@class="t4"]/text()').extract()
            joblink   = jobitem.xpath('p/span/a/@href').extract()[0]
            item['jobname'] = jobnames
            item['company'] = companys
            item['salary'] = salarys
            jobrequest = scrapy.Request(joblink,callback=self.parse_job)
            jobrequest.meta['item'] = item
            yield jobrequest
        
        nextpage  = response.xpath('//div[@class="dw_page"]//li[@class="bk"]')[1]
        try:
            nextpagelink = nextpage.xpath('a/@href').extract()[0]
    
            yield  scrapy.Request(nextpagelink,callback=self.parse)
        except:
            print 'end of page'
        


    def parse_job(self, response):
   
        item = response.meta['item']

        content = [] 

        '''
        for text in response.xpath('//div[@class="bmsg job_msg inbox"]/text()').extract():
            content.append(text.strip())
        for text in response.xpath('//div[@class="bmsg job_msg inbox"]/p/text()').extract():
            content.append(text.strip())
        '''
        for text in response.xpath('//div[@class="bmsg job_msg inbox"]//text()').extract():
            content.append(text.strip())

        item['jobcont'] = ''.join(content).strip()
        return item
