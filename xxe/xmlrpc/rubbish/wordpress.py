# encoding:utf-8
'''
WordPress采用了XML-RPC接口.并且通过内置函数WordPress API实现了该接口内容 
 *从3.5版本开始，XML-RPC功能默认开启 
 *1.可以查看wordpress系统允许的方法
 *2.帐号爆破
 *3.ssrf
 *4.读取文件
 *
'''
 #!/usr/bin/python
import requests
import sys
def posturl(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0','Host': "",'Accept': 'text/html,application/xhtml+xml,application/json','Accept-Language': 'zh-cn,zh;q=0.5,en-US','Accept-Encoding': 'gzip,deflate',"content-Type": "application/x-www-form-urlencoded","Cookie": "JSESSIONID=EA01FF2B025861F39E29712C97F7DF69;"}
    datas = '<?xml version= "1.0"?>'\
            '<methodCall>'\
            '<methodName>system.listMethods/methodName>'\
            '</methodCall>'
    r = requests.post(url,data=datas, headers=headers)
    print(r.text)
    if r.status_code==200:
       print(r.text)
    else:
       print("erro")
posturl(sys.argv[1])
