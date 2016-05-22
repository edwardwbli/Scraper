# -*- coding: utf-8 -*-

import scrapy
from googledp.items import GoogledpItem

class gglSpider(scrapy.Spider):
    name = "ggldp"
    allowed_domains = ["google.com"]
    start_urls = [
        'http://tushare.waditu.com/'
       
     ]

    def parse(self, response):
        rootpath = 'http://tushare.waditu.com/%s'
        for sel in response.xpath('//li[@class="toctree-l2"]'):
            item = GoogledpItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = [rootpath %a for a in sel.xpath('a/@href').extract()]
            yield item
