# -*- coding: utf-8 -*-
#scrapy crawl 51job -a qk='scrapy' -o item.csv
#qk for search keyword in 51Job
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy_splash import SplashRequest
from zljob.items import ZljobItem


class Jobsearch(scrapy.Spider):
    name = "zljob"
    allowed_domains = ["zhaopin.com"]

    def __init__(self,kw='python'):
        self.start_urls = ["http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%B9%BF%E5%B7%9E&kw=" + kw + "&sm=0&p=1"]
    
    def parse(self, response):
        #using >> in scrapy: scrapy crawl zljob >> log.txt will direct print output to log.txt only
        #print response.body
        

        joblist =  response.xpath('//table[@class="newlist"]')
        joblist.pop(0)
        for jobitem in joblist:
            #must create multiple items corresponding to every new scrapy request
            #if just create single item outside for loop
            #this item will overide until the end of the jobrequest list
            #yield to be a generator with same item reference,
            #
            item = ZljobItem()
            
            jobnames  = ''.join(jobitem.xpath('tr[1]/td[@class="zwmc"]/div/a//text()').extract()).strip()
            joblink   = jobitem.xpath('tr[1]/td[@class="zwmc"]/div/a/@href').extract()[0]

            companys  = jobitem.xpath('tr[1]/td[@class="gsmc"]/a//text()').extract()
            companylink =  jobitem.xpath('tr[1]/td[@class="gsmc"]/a/@href').extract()[0]

            salarys   = jobitem.xpath('tr[1]/td[@class="zwyx"]/text()').extract()
            location = jobitem.xpath('tr[1]/td[@class="gzdd"]/text()').extract()
            contentabbr = ''.join(jobitem.xpath('tr[2]//li[@class="newlist_deatil_last"]//text()').extract()).strip()

            
            item['jobname'] = jobnames
            item['company'] = companys
            item['salary'] = salarys
            item['joblocation'] = location
            item['jobcontabbr'] = contentabbr
            yield item
    
        try:
            nextpagelink = response.xpath('//div[@class="pagesDown"]//li[@class="pagesDown-pos"]/a/@href').extract()[0]
            
            yield  scrapy.Request(nextpagelink,callback=self.parse)
        except:
            print 'end of page'


    def parse_job(self, response):
        pass