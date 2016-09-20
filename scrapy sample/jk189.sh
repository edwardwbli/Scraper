#! /bin/ksh

curl_doctor_detail() {
#function to get all doctor detail info

echo 'http://189jk.cn/api/hospital/department_schedule/'$hosid'/'$dpid'/1/1.do'
curl 'http://189jk.cn/api/hospital/department_schedule/'$hosid'/'$dpid'/1/1.do' -H 'Cookie: JSESSIONID=aaaT7IFxaw_eo8HQozYvv; tencentSig=8764854272; _qdda=2-1.1; _qddab=2-13xup7.iq88axw5; _qddac=2-1.1.13xup7.iq88axw5; Hm_lvt_e8e882fc1ed9a6c49d45baa9a5464ff6=1467471866,1467511985,1467512111,1467514274; Hm_lpvt_e8e882fc1ed9a6c49d45baa9a5464ff6=1467649967' -H 'Origin: http://189jk.cn' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36' -H 'Content-Type: application/json' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Cache-Control: max-age=0' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' -H 'Referer: http://189jk.cn/?view=public/department_info&hospitalId=422&departmentId=189202' --data-binary 'null' --compressed >> $dr_detail_file
};

scrape_doctor() {

for i in `cat $dpfile | grep -oE '\"departmentId\":\"(.*?)\"' | cut -c17-22 | sed 's/\"//g' | sort`;do

#it seem that below for loop cat all files in list of $dpmentfile if it's a list of files
#for i in `cat $dpmentfile | grep -oE '\"departmentId\":\"(.*?)\"' | cut -c17-22 | sed 's/\"//g' | sort`;do

    dpid=$i
    dr_detail_file=$hosdir'/dp'$dpid'doclist.json'
    #filesize=`ls -l $dr_detail_file | awk '{ print $5 }'`

    if  [[ ! -e $dr_detail_file  ]] ; then
       curl_doctor_detail
       sleep 5

    fi;

done;
};

scrap_doctor_with_hoslist() {

    dpmentfile=`ls -la ./hos_rawdata/all_GZ_hos_department/hos*.json | awk '{ print $9 }'`
    for dpfile in $dpmentfile;do
        hosid=`echo $dpfile | sed 's/.*hos//g' | sed 's/\.json//g'`
        hosdir='./hos_rawdata/hos'$hosid'/'
        mkdir $hosdir
        echo $hosdir
        scrape_doctor

    done;

}


#Run Function

scrap_doctor_with_hoslist
