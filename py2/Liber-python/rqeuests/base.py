#!/usr/bin/env python
# -*- coding:utf-8 -*-


r = requests.get('http://www.zhidaow.com')
r = requests.post("http://httpbin.org/post")
r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")
r = requests.head("http://httpbin.org/get")
r = requests.options("http://httpbin.org/get")

