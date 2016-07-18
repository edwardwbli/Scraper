# coding = utf-8
import os
import time
import json
import sys
#print os.system("curl 'http://189jk.cn/api/hospital/list_base_info/1.do' -H 'Cookie: JSESSIONID=aaaT7IFxaw_eo8HQozYvv; tencentSig=8764854272; _qdda=2-1.358lpu; _qddab=2-z3pggi.iq64tioi; Hm_lvt_e8e882fc1ed9a6c49d45baa9a5464ff6=1467471866,1467511985,1467512111,1467514274; Hm_lpvt_e8e882fc1ed9a6c49d45baa9a5464ff6=1467522460' -H 'Origin: http://189jk.cn' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36' -H 'Content-Type: application/json' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Cache-Control: max-age=0' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' -H 'Referer: http://189jk.cn/' --data-binary 'null' --compressed")

jsondata = json.loads(sys.stdin)
print jsondata


curl 'http://189jk.cn/api/hospital/list_base_info/1.do' -H 'Cookie: JSESSIONID=aaaT7IFxaw_eo8HQozYvv; tencentSig=8764854272; _qdda=2-1.358lpu; _qddab=2-z3pggi.iq64tioi; Hm_lvt_e8e882fc1ed9a6c49d45baa9a5464ff6=1467471866,1467511985,1467512111,1467514274; Hm_lpvt_e8e882fc1ed9a6c49d45baa9a5464ff6=1467522460' -H 'Origin: http://189jk.cn' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36' -H 'Content-Type: application/json' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Cache-Control: max-age=0' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' -H 'Referer: http://189jk.cn/' -H 'Content-Length: 4' --data-binary 'null' --compressed

curl 'http://189jk.cn/api/hospital/departments_base_info/939.do' -H 'Cookie: JSESSIONID=aaaT7IFxaw_eo8HQozYvv; tencentSig=8764854272; _qdda=2-1.358lpu; _qddab=2-z3pggi.iq64tioi; Hm_lvt_e8e882fc1ed9a6c49d45baa9a5464ff6=1467471866,1467511985,1467512111,1467514274; Hm_lpvt_e8e882fc1ed9a6c49d45baa9a5464ff6=1467522460' -H 'Origin: http://189jk.cn' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36' -H 'Content-Type: application/json' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: http://189jk.cn/' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --data-binary 'null' --compressed