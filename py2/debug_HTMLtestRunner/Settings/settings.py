#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: v1.0
@author: Bryan.Lan
@contact: 244896035@qq.com
@site: http://http://blog.csdn.net/weixin_36650524
@time: 2017/11/8 17:23
"""

class Settings(object):
    """
    存储接口测试的所以设置的类
    """

    def __init__(self):
        self.host = "http://192.168.3.6"

class AccountSettings(object):
    """
    存储Account服务相关设置
    """

    def __init__(self):
        self.login_path = "/v1/account/login"
