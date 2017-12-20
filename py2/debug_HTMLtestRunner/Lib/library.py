#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: v1.0
@author: Bryan.Lan
@contact: 244896035@qq.com
@site: http://http://blog.csdn.net/weixin_36650524
@time: 2017/11/8 17:26
"""

#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import json
from Settings.settings import Settings, AccountSettings


class Account(object):
    """login email"""

    def __init__(self):
        self.set = Settings()
        self.Accset = AccountSettings()

    def login_email(self, email, password):
        url = self.set.host + self.Accset.login_path
        data = {
            'email': email,
            "password": password
        }
        headers = {'content-type': 'application/json'}

        res = requests.post(url, data=json.dumps(data), headers=headers)
        return res

    def get_acc_info(self, ACCESS_TOKEN, EMAIL):
        url = self.set.host + "/v1/account" + '?' + 'email=' + EMAIL
        headers = {
            'content-type': 'application/json',
            'authorization': ACCESS_TOKEN
        }

        res = requests.get(url, headers=headers)
        return res
