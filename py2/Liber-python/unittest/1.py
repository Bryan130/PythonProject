#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 通过unittest.main()来执行测试用例的方式


import unittest

class UCTestCase(unittest.TestCase):
    def setUp(self):
        #测试前需执行的操作
        pass

    def tearDown(self):
        #测试用例执行完后所需执行的操作
        pass

    # 测试用例1
    def testCreateFolder(self):
        #具体的测试脚本
        pass

    # 测试用例2
    def testDeleteFolder(self):
        #具体的测试脚本
        pass


if __name__ == "__main__":
    unittest.main()
