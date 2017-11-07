#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests

# 采集时为避免被封IP，经常会使用代理。requests也有相应的proxies属性。

proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}

requests.get("http://www.zhidaow.com", proxies=proxies)

# 如果代理需要账户和密码，则需这样：

proxies = {
    "http": "http://user:pass@10.10.1.10:3128/",
}
