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
import Settings.settings as setter


class Account(object):
    """login email"""

    def __init__(self):
        self.set = setter.Settings()
        self.Acc_set = setter.AccountSettings()

    def login_email(self, email, password):
        """
        Account服务登陆接口
        :param email:
        :param password:
        :return:
        """
        url = self.set.host + self.Acc_set.login_path
        data = {
            'email': email,
            "password": password
        }
        headers = {'content-type': 'application/json'}

        res = requests.post(url, data=json.dumps(data), headers=headers)
        return res

    def get_acc_info(self, access_token, email):
        """
        Account服务获取账户信息接口
        :param access_token:
        :param email:
        :return:
        """
        url = self.set.host + "/v1/account" + '?' + 'email=' + email
        headers = {
            'content-type': 'application/json',
            'authorization': access_token
        }

        res = requests.get(url, headers=headers)
        return res
