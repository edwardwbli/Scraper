# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    doctor =  scrapy.Field()
    position = scrapy.Field()
    profession = scrapy.Field()
    workhour = scrapy.Field()


class YihuItemhos(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hospitalId =  scrapy.Field()
    hosName = scrapy.Field()
    hosGuid = scrapy.Field()
    hosDeptId = scrapy.Field()
    deptName = scrapy.Field()
    bigDepartmentSn = scrapy.Field()