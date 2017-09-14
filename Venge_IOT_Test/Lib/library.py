#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import json
from Settings.settings import Settings


class Account(object):
    """login email"""
    def __init__(self):
        self.set = Settings()

    def login_email(self, email, password):
        url = self.set.host + "/v1/account/login"
        data = {'email': email, "password":password}
        headers = {'content-type': 'application/json'}

        res = requests.post(url, data=json.dumps(data), headers=headers)
        return res

    def get_acc_info(ACCESS_TOKEN, EMAIL):
        url = self.set.host + "/v1/account" + '?' + 'email=' + EMAIL
        headers = {'content-type': 'application/json', 'authorization': ACCESS_TOKEN}

        res = requests.get(url, headers=headers)
        return res

