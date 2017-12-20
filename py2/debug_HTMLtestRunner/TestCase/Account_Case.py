#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: v1.0
@author: Bryan
@contact: 244896035@qq.com
@site: http://http://blog.csdn.net/weixin_36650524
@time: 2017/11/8 16:49
"""


import os
import unittest
from Lib import library

class TestAccountAPI(unittest.TestCase):
    def setUp(self):
        self.Acc = library.Account()
        pass

    def tearDown(self):
        pass

    def test_login_acoount(self):
        """
        验证登录企业账户
        :return:
        """
        # 登陆企业账户
        self.ret = self.Acc.login_email("Bryan@qq.com", "bryan123")
        # print(self.ret.json())

        # 解析数据

        # 验证结果
        self.assertEqual(self.ret.status_code, 200, msg="reuqests failed")

    def test_login_acoount_email_error(self):
        """
        验证登录企业账户
        :return:
        """
        # 登陆企业账户
        self.ret = self.Acc.login_email("Bryan1234@qq.com", "bryan123")
        # print(self.ret.json())

        # 解析数据

        # 验证结果
        self.assertEqual(self.ret.status_code, 400, msg="reuqests failed")

    def test_login_acoount_email_error2(self):
        """
        验证登录企业账户
        :return:
        """
        # 登陆企业账户
        self.ret = self.Acc.login_email("Bryan111@qq.com", "bryan123")

        # 解析数据

        # 验证结果
        self.assertEqual(self.ret.status_code, 200, msg="reuqests failed")

if __name__ == "__main__":
    # 装载测试用例
    test_cases = unittest.TestLoader().loadTestsFromTestCase(TestAccountAPI)
    # 使用测试套件并打包测试用例
    test_suit= unittest.TestSuite()
    test_suit.addTests(test_cases)
    # 运行测试套件，并返回测试结果
    test_result = unittest.TextTestRunner(verbosity=1).run(test_suit)
    # 生成测试报告
    # print("testsRun:%s" % test_result.testsRun)
    # unittest.main()
