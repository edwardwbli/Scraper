# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZljobItem(scrapy.Item):
    # define the fields for your item here like:
    jobname = scrapy.Field()
    company = scrapy.Field()
    salary = scrapy.Field()
    jobcontabbr = scrapy.Field()
    joblocation = scrapy.Field()