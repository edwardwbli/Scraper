#! /bin/ksh

curl_init() {
curl 'http://189jk.cn/' -H 'Cookie: JSESSIONID=aaaT7IFxaw_eo8HQozYvv; tencentSig=8764854272; _qdda=2-1.1; _qddab=2-13xup7.iq88axw5; _qddac=2-1.1.13xup7.iq88axw5; Hm_lvt_e8e882fc1ed9a6c49d45baa9a5464ff6=1467471866,1467511985,1467512111,1467514274; Hm_lpvt_e8e882fc1ed9a6c49d45baa9a5464ff6=1467649967' -H 'Origin: http://189jk.cn' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36' -H 'Content-Type: application/json' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Cache-Control: max-age=0' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' -H 'Referer: http://189jk.cn/?view=public/department_info&hospitalId=422&departmentId=189202' --data-binary 'null' --compressed
};

curl_doctor_detail() {
#function to get all doctor detail info

echo 'http://189jk.cn/api/hospital/department_schedule/'$hosid'/'$dpid'/1/1.do'
curl 'http://189jk.cn/api/hospital/department_schedule/'$hosid'/'$dpid'/1/1.do' -H 'Cookie: JSESSIONID=aaaT7IFxaw_eo8HQozYvv; tencentSig=8764854272; _qdda=2-1.1; _qddab=2-13xup7.iq88axw5; _qddac=2-1.1.13xup7.iq88axw5; Hm_lvt_e8e882fc1ed9a6c49d45baa9a5464ff6=1467471866,1467511985,1467512111,1467514274; Hm_lpvt_e8e882fc1ed9a6c49d45baa9a5464ff6=1467649967' -H 'Origin: http://189jk.cn' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36' -H 'Content-Type: application/json' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Cache-Control: max-age=0' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' -H 'Referer: http://189jk.cn/?view=public/department_info&hospitalId=422&departmentId=189202' --data-binary 'null' --compressed >> $dr_detail_file
};

curl_doctor_list() {
#function to get all doctor base info

 dr_base_file='./hos_rawdata/hos399/dp'$dpid'doclist_base.json'
 echo 'http://189jk.cn/api/hospital/doctors_base_info/'$hosid'/'$dpid'.do'
 curl 'http://189jk.cn/api/hospital/doctors_base_info/'$hosid'/'$dpid'.do' -H 'Cookie: JSESSIONID=aaaT7IFxaw_eo8HQozYvv; tencentSig=8764854272; Hm_lvt_e8e882fc1ed9a6c49d45baa9a5464ff6=1467471866,1467511985,1467512111,1467514274; Hm_lpvt_e8e882fc1ed9a6c49d45baa9a5464ff6=1467638066; _qdda=2-1.1; _qddab=2-864q5v.iq81evrw' -H 'Origin: http://189jk.cn' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36' -H 'Content-Type: application/json' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: http://189jk.cn/' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --data-binary 'null' --compressed >> $dr_base_file
};

scrape_doctor() {
#scrap doctor info
hosid=399
dpmentfile='./hos_rawdata/all_GZ_hos_department/hos'$hosid'.json'

for i in `cat $dpmentfile | grep -oE '\"departmentId\":\"(.*?)\"' | cut -c17-22 | sed 's/\"//g' | sort`;do
    dpid=$i
    dr_detail_file='./hos_rawdata/hos399/dp'$dpid'doclist.json'
    #filesize=`ls -l $dr_detail_file | awk '{ print $5 }'`

    if  [[ ! -e $dr_detail_file  ]] ; then
       curl_doctor_detail
       sleep 5

    fi;

done;
};

scrape_deparment() {
ctyid=1
ctyhosfile='./hos_rawdata/all_CN_Hos/cty'$ctyid'.json'

for i in `cat $ctyhosfile | grep -oE '\"hospitalId\":\"(.*?)\"' | cut -c15-19 | sed 's/\"//g'`;do
    hosid=$i
    hos_dp_file='./hos_rawdata/all_GZ_hos_department/hos'$hosid'.json'
    curl 'http://189jk.cn/api/hospital/departments_base_info/'$hosid'.do'  -H 'Cookie: JSESSIONID=aaaT7IFxaw_eo8HQozYvv; tencentSig=8764854272; _qddac=2-1.1.864q5v.iq81evrw; Hm_lvt_e8e882fc1ed9a6c49d45baa9a5464ff6=1467471866,1467511985,1467512111,1467514274; Hm_lpvt_e8e882fc1ed9a6c49d45baa9a5464ff6=1467637415; _qdda=2-1.1; _qddab=2-864q5v.iq81evrw' -H 'Origin: http://189jk.cn' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36' -H 'Content-Type: application/json' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Cache-Control: max-age=0' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' -H 'Referer: http://189jk.cn/' --data-binary 'null' --compressed >> $hos_dp_file
    sleep 2
done;

}

scrape_hos() {
prevctid=0
for i in `cat ./hos_rawdata/city.json | grep -oE '\"cityId\":\"(.*?)\"' | cut -c11-19 | sed 's/\"//g'`;do

    ctid=$i
    if [[ $ctid != $prevctid ]] ; then
        filename='./hos_rawdata/all_CN_Hos／cty'$ctid'.json'
        echo 'http://189jk.cn/api/hospital/list_base_info/'$ctid'.do'
        curl 'http://189jk.cn/api/hospital/list_base_info/'$ctid'.do' -H 'Cookie: JSESSIONID=aaaT7IFxaw_eo8HQozYvv; tencentSig=8764854272; _qdda=2-1.358lpu; _qddab=2-z3pggi.iq64tioi; Hm_lvt_e8e882fc1ed9a6c49d45baa9a5464ff6=1467471866,1467511985,1467512111,1467514274; Hm_lpvt_e8e882fc1ed9a6c49d45baa9a5464ff6=1467522460' -H 'Origin: http://189jk.cn' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36' -H 'Content-Type: application/json' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Cache-Control: max-age=0' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' -H 'Referer: http://189jk.cn/' --data-binary 'null' --compressed >> $filename
        sleep 3
        prevctid=$i
    fi;
done;

}

#curl_init
scrape_doctor
#scrape_deparment


