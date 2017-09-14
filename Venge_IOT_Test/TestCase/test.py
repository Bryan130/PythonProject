#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
import os, sys
pwd = os.getcwd()
father_path=os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")
print "当前文件路径:",father_path
sys.path.append(father_path)

from Lib.library import Account


if __name__ == '__main__':
    lo = Account()
    email = "Bryan@qq.com"
    password = "bryan123"
    res = lo.login_email(email, password)
    print "return code: ",res.status_code
    res_dict = res.json()
    ACCESS_TOKEN = res_dict['access_token']
    print ACCESS_TOKEN

    res = lo.
