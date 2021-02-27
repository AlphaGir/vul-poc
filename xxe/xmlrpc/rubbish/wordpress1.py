import sys
import os
'''
x=sys.argv[1]
a="curl "+x+"/xmlrpc.php"+" -d "+'<?xml version="1.0" encoding="UTF-8"?><methodCall><methodName>system.listMethods</methodName></methodCall>'
'''
'''
tmp = os.popen(a).readlines()
print(tmp)
'''
import subprocess
p = subprocess.Popen('curl '+"https://example.com/action/xmlrpc"+" -d "+ '<?xml version="1.0" encoding="UTF-8"?><methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value>{USERNAME}</value></param><param><value>{PASSWORD}</value></param></params></methodCall>')
for line in p:
    print line
