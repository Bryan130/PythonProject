#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 基本身份认证(HTTP Basic Auth):

import requests
from requests.auth import HTTPBasicAuth

r = requests.get('https://httpbin.org/hidden-basic-auth/user/passwd', auth=HTTPBasicAuth('user', 'passwd'))
# r = requests.get('https://httpbin.org/hidden-basic-auth/user/passwd', auth=('user', 'passwd'))    # 简写
print(r.json())

# 另一种非常流行的HTTP身份认证形式是摘要式身份认证，Requests对它的支持也是开箱即可用的:

requests.get(URL, auth=HTTPDigestAuth('user', 'pass'))
