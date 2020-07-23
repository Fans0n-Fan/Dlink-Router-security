# -*- coding:UTF-8 -*-
#!/usr/bin/env python2
import requests

IP='192.168.10.1'
datas ='<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><SetWanSettings xmlns="http://purenetworks.com/HNAP1/"><Type>Static</Type><PppoeType></PppoeType><Username></Username><Password></Password><MaxIdleTime>0</MaxIdleTime><MTU>1500</MTU><HostName></HostName><ServiceName></ServiceName><AutoReconnect>false</AutoReconnect><IPAddress>192.168.8.106</IPAddress><SubnetMask>255.255.255.0</SubnetMask><Gateway>192.168.8.1</Gateway><DnsManual>true</DnsManual><MacCloneEnable>false</MacCloneEnable><CloneMacAddress></CloneMacAddress><MacCloneType></MacCloneType><WanSpeed>Auto</WanSpeed><WanDuplex>Auto</WanDuplex><ConfigDNS><Primary>114.114.114.88</Primary><Secondary></Secondary></ConfigDNS><MacAddress></MacAddress><VPNServerIPAddress></VPNServerIPAddress><VPNLocalIPAddress></VPNLocalIPAddress><VPNLocalSubnetMask></VPNLocalSubnetMask><VPNLocalGateway></VPNLocalGateway></SetWanSettings></soap:Body></soap:Envelope>'
length = len(datas)

headers = requests.utils.default_headers()
headers["Content-Length"]=str(length)
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36"
headers["SOAPAction"] = '"http://purenetworks.com/HNAP1/SetWanSettings"'#此处的Login可以替换为任何在function_list中的函数名
headers["Content-Type"] = "text/xml; charset=UTF-8"
headers["Accept"]="*/*"
headers["Accept-Encoding"]="gzip, deflate"
headers["Accept-Language"]="zh-CN,zh;q=0.9,en;q=0.8"
headers["HNAP_AUTH"]="E21E513ECE4586A72F9D3932B655F90D 1573789905"
headers["X-Requested-With"]="XMLHttpRequest"
headers["Origin"]="http://192.168.10.1"
headers["Connection"]="close"
headers["Referer"]="http://192.168.10.1/Network.html"
headers["Cookie"]="bLanguage=en; uid=NEy5R3U29u; PrivateKey=9C0765BB6F6A6F1E89224E0D55F37882"

r = requests.post('http://'+IP+'/HNAP1/', headers=headers, data=datas)
print r.text
