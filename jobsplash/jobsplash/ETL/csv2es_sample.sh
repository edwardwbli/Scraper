#! /usr/bin/env bash

#pip install csv2es, before excuting below command
csv2es --index-name job --doc-type scalajob --import-file scala.csv --delimiter ',' --delete-index
#check mapping after load
curl -XGET  "http://127.0.0.1:9200/job/_mapping/scalajob?pretty"

#load data to es with mapping file of fields
#?????


#search all
curl -XGET http://127.0.0.1:9200/job/_search?pretty

#get company name including "广州市柏纳管理顾问有限公司"
curl -XGET "http://127.0.0.1:9200/job/_search?q=company:%22%E5%B9%BF%E5%B7%9E%E5%B8%82%E6%9F%8F%E7%BA%B3%E7%AE%A1%E7%90%86%E9%A1%BE%E9%97%AE%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%22&pretty"

#get company name including "汇丰", and return jobname and jobcontent only
curl -XGET "http://127.0.0.1:9200/job/_search?q=company:%22%E6%B1%87%E4%B8%B0%22&_source=jobname%2Cjobcont&pretty"

#get company list aggregations(group by, and remove duplication),
#Causion:
#-d after should use '' instead of "" for the json quotation,
#if not, will cause json_parse_exception, with reason "Unrecognized token 'company': was expecting ('true', 'false' or 'null')"
curl -XGET "http://127.0.0.1:9200/job/_search?pretty" -d '
{
    "size": 0,
    "aggs": {
    "companys": {

           "terms": {"field": "company"}

        }
    }
}
'

#Set custome analyzer, with creating new index
curl -XPOST "http://127.0.0.1:9200/job" -d '
{
   "settings": {
     "analysis": {
      "analyzer" : {
        "job_analyzer": {
            "type": "custom",
            "tokenizer":   "keyword"

}
}
}
}
}
'


#Set customer analyzer, without creating new index,
#1. can't use post method, or will hit {"error":{"root_cause":[{"type":"invalid_type_name_exception","reason":"Document mapping type name can't start with '_'"}]
#2. must close index, before updating, after updating index, we need to open again.
#close index
#available value of tokenizer keyword, whitespace
curl -XPOST 'localhost:9200/job/_close'

curl -XPUT "http://127.0.0.1:9200/job/_settings" -d '
{

"analysis": {
"analyzer" : {
"job_analyzer": {
"type": "custom",
"tokenizer":   "whitespace"


}
}
}
}
'
#open index
curl -XPOST 'localhost:9200/job/_open'

#test analyzer
curl -XGET "http://127.0.0.1:9200/job/_analyze?analyzer=job_analyzer" -d '集群内部工作方式'
#response
#{"tokens":[{"token":"集群内部工作方式","start_offset":0,"end_offset":8,"type":"word","position":0}]}
#or
curl -XGET "http://127.0.0.1:9200/_analyze?analyzer=standard&text=Text to analyze"


#field statistics
curl -XGET "http://localhost:9200/job/_field_stats?fields=company"




