# -*- coding: utf-8 -*-
import json
import scrapy
from scrapy.http import FormRequest,Request

#from scrapy_splash import SplashRequest
from yihu.items import YihuItem,YihuItemhos
from selenium import webdriver
import os
import time
from yihu.settings import *
class yihuspider(scrapy.Spider):
    name = "yihu"
    #allowed_domains = ["http://www.yihu.com/"]
        #start_urls = [
        #         "http://www.yihu.com/QuickReg/doGetHospitalListByCityId"
        #         ]
    def start_requests(self):
        frmdata = {'city_id': '200'}
        url = "http://www.yihu.com/QuickReg/doGetHospitalListByCityId"
        return [FormRequest(url, callback=self.parse, formdata=frmdata)]
    
    def parse(self, response):
        jsondata = json.loads(response.body)

        for hos in jsondata:
            item = YihuItemhos()
            item['hospitalId'] = hos['hospitalId']
            item['hosName'] = hos['hosName']
            item['hosGuid'] = hos['hosGuid']
            '''yield item'''

            url = "http://www.yihu.com/QuickReg/doGetDepartmentListByHospitalId"
            frmdata = {'hospital_id': item['hospitalId']}
            request = FormRequest(url, callback=self.parse_dep, formdata=frmdata)
            request.meta['item'] = item
            yield request

    def parse_dep(self,response):
        item = response.meta['item']
        jsondata = json.loads(response.body)

        for dep in jsondata:
            item['hosDeptId'] = dep['hosDeptId']
            item['deptName'] = dep['deptName']
            item['bigDepartmentSn'] = dep['bigDepartmentSn']
            yield item

class yjkspider(scrapy.Spider):
    name = "yjk"
    
    #def __init__(self):
    #    self.headers = HEADER
        #self.cookies =COOKIES
    #allowed_domains = ["http://www.yihu.com/"]
    #start_urls = [
    #         "http://www.yihu.com/QuickReg/doGetHospitalListByCityId"
    #         ]
    #http://189jk.cn/api/init/all_cities.do get city list
    #http://189jk.cn/api/hospital/list_base_info/1.do get hospital list on city id
    #http://189jk.cn/api/hospital/departments_base_info/939.do get department list on hospital id
    #http://189jk.cn/api/hospital/doctors_base_info/939/214935.do get doctors list on deparment id
    #http://189jk.cn/api/hospital/doctor_schedule/939/214935/427796.do get doctor info on doctor id
    def start_requests(self):
        url = "http://189jk.cn/?view=public%2Fdoctor&cityId=1&hospitalId=939&departmentId=214935&doctorId=427796"
        yield FormRequest(url,callback=self.parse)
    
    def parse(self, response):
        doctorname  = response.xpath('//*[@id="doctor-name"]/text()').extract()
        doctortitle = response.xpath('//*[@id="doctor-title"]/text()').extract()
        print doctortitle
