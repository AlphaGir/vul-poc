#!/bin/bash/python
import os

data = ['www.baidu.com',
'www.csdn.cn']
t1="curl http://www.adminxe.com/xmlrpc.php"+" -d "+'<?xml version="1.0" encoding="UTF-8"?><methodCall><methodName>system.listMethods</methodName></methodCall>'
print(t1)
tmpres = os.popen(t1).readlines()
print(tmpres)

