#! /bin/ksh

scrape_hos() {

curl 'https://yi.baidu.com/pc/hospital/listregion?provId=4&cityId=84&regionId=all&page=1&pageSize=10&seed=seed_1468939350601' -H 'Cookie: __cfduid=dcd593e474aab661a435678fb5495ace11464535831; BAIDUID=0AF759FBB0DE83F3A1B560D86DABAF2D:FG=1; PSTM=1468068667; BIDUPSID=89ECD343764C3C302D2549D5C886D439; BDUSS=VWVFg0b2hOVX5wQnlRZ0pvOGd3RnZzTFllOWNkSENBZ1ZNaHZEalpSWS00YXRYQUFBQUFBJCQAAAAAAAAAAAEAAAAYxmM6AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5UhFc-VIRXSl; cflag=15%3A3; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDRCVFR[bCS10QISK_f]=mk3SLVN4HKm; H_PS_PSSID=1461_17758_18241_17946_20415_15340_11731; pgv_pvi=9795344384; pgv_si=s5612356608; tssid=pcNewHospitalPage%3A2; Hm_lvt_2129ef9891a442299befc9c664fc73e3=1468939328; Hm_lpvt_2129ef9891a442299befc9c664fc73e3=1468939328' -H 'Accept-Encoding: gzip, deflate, sdch, br' -H 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: https://yi.baidu.com/pc' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --compressed >> log.txt

}

scrape_hos


