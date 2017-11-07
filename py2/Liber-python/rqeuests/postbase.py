#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
import json

data = {'some': 'data'}
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

r = requests.post('https://api.github.com/some/endpoint', data=data, headers=headers)
print(r.text)


requests.get('http://www.dict.baidu.com/s', params={'wd': 'python'})    #GET参数实例
requests.post('http://www.itwhy.org/wp-comments-post.php', data={'comment': '测试POST'})    #POST参数实例
