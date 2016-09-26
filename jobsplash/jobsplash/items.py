# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Job51SearchItem(scrapy.Item):
    # define the fields for your item here like:
    jobid = scrapy.Field()
    jobname = scrapy.Field()
    company = scrapy.Field()
    salary = scrapy.Field()
    jobcont = scrapy.Field()
    # name = scrapy.Field()

