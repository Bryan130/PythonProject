#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests

url = 'http://127.0.0.1:5000/upload'
files = {'file': open('/home/lyb/sjzl.mpg', 'rb')}
#files = {'file': ('report.jpg', open('/home/lyb/sjzl.mpg', 'rb'))}     #显式的设置文件名

r = requests.post(url, files=files)
print(r.text)



# 你可以把字符串当着文件进行上传：

import requests

url = 'http://127.0.0.1:5000/upload'
files = {'file': ('test.txt', b'Hello Requests.')}     #必需显式的设置文件名

r = requests.post(url, files=files)
print(r.text)
