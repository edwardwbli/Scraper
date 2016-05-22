# -*- coding: utf-8 -*-

import scrapy
from googledp1.items import GoogledpItem
keyword = "Python"
#把字符串编码成符合url规范的编码
keywordcode = urllib.quote(keyword)
class gglSpider(scrapy.Spider):
    name = "ggldp"
    allowed_domains = ["google.com"]
    '''start_urls = [
        'https://www.google.com/search?q=scrapy&num=100&ie=utf-8&oe=utf-8&aq=t&rls=org.mozilla:en-US:official&client=firefox-a&channel=fflb'
       
     ]'''
    def start_requests(self):
        return [scrapy.FormRequest('https://www.google.com/search?q=scrapy&num=10&ie=utf-8&oe=utf-8&aq=t&rls=org.mozilla:en-US:official&client=firefox-a&channel=fflb')]
    
    def parse(self, response):

        for sel in response.xpath('//h3[@class="r"]'):
            item = GoogledpItem()
            item['title'] = sel.xpath('a/text()').re(r'(.*)')
            item['link'] = sel.xpath('a/@href').re(r'\/url\?q=(.*)')
            yield item
