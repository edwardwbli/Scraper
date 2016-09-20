# coding = utf-8
import pandas as pd
import numpy as np
import os,optparse
import json
import re
from pandas.io.json import json_normalize
from pandas import read_json
import glob

JSON_FILE_PATH = './hos_rawdata/hos422/doclist.json'
FILEDIR = '/Users/wangshidi/ProjectA/Python/Scraper/yihu/'

def parse_args():
    usage = """usage: python j2cpaser.py filename
    to grab detail from files
    or 
    python j2cpaser.py hos_rawdata/hos*/dp* will got list of files
    
    """

    parser = optparse.OptionParser(usage)

    _, filename = parser.parse_args()

    def parse_file_path(filename):
        
        return FILEDIR + filename

    return map(parse_file_path, filename)

def j2c(json_file_path):
    json_file = open(json_file_path)
    jsonrsp = json.load(json_file)['response']
    if len(jsonrsp) != 0:
        df = pd.DataFrame(json_normalize(jsonrsp))
        df.to_csv('./hos_rawdata/doclist.csv',
              encoding='utf8',
              mode='a+',
              index=False,
              header=False,
              columns=[
                  'hospitalName',
                  'departmentName',
                  'doctorName',
                  'title',
                  'sex',
                  'specialty'
              ])
   
def j2c_spc(json_file_path):
    print json_file_path
    json_file = open(json_file_path)
    '''
        json_data = re.sub(r'}{','}\,{',json_file.read())
        data = '[' + json_data + ']'
        json_data = json.loads(data)
        print json_normalize(json_data)
        '''
    df = pd.DataFrame()
    for line in json_file:
        jsonobj_list = line.split('}{')
      
        for jsonobj in jsonobj_list:
            if re.search(r'^\{',jsonobj):
                jsonobj = jsonobj + '}'
                jsonrsp = json.loads(jsonobj)['response']
                if len(jsonrsp) != 0:
                    df = df.append(json_normalize(jsonrsp))
        
            elif re.search(r'\}$',jsonobj):
                jsonobj = '{' + jsonobj
                #data.append(json.loads(jsonobj)['response'])
                jsonrsp = json.loads(jsonobj)['response']
                if len(jsonrsp) != 0:
                    
                    df = df.append(json_normalize(jsonrsp))

            else:
                jsonobj = '{' + jsonobj +'}'
                #data.append(json.loads(jsonobj)['response'])
                jsonrsp = json.loads(jsonobj)['response']
                if len(jsonrsp) != 0:
                    
                    df = df.append(json_normalize(jsonrsp))

    df.to_csv('./hos_rawdata/hos422/doclist.csv',
              encoding='utf8',
              mode='a+',
              index=False,
              columns=[
                  'hospitalName',
                  'departmentName',
                  'doctorName',
                  'title',
                  'sex',
                  'specialty'
              ])
   
                
    #df =  pd.read_csv('yihuhos.csv')
    #drop duplicates
    #df.drop_duplicates(subset='hosName')['hosName']


if __name__ == '__main__':
    file = parse_args()
    for f in file:
        print f
        j2c(f)
