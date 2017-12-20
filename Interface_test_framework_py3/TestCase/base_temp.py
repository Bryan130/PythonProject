#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: v1.0
@author: Bryan.Lan
@contact: 244896035@qq.com
@site: http://http://blog.csdn.net/weixin_36650524
@time: 2017/11/8 20:09
"""

import time
import unittest
import HTMLTestRunner

class UCTestCase(unittest.TestCase):
    def setUp(self):
        """
        前置条件
        :return:
        """
        pass

    def tearDown(self):
        """
        收尾工作
        :return:
        """
        pass

    def testCreateFolder(self):
        """
        测试用例1
        :return:
        """
        pass

    def testDeleteFolder(self):
        """
        测试用例2
        :return:
        """
        pass


if __name__ == "__main__":
    test_unit=unittest.TestSuite()
    # 将测试用例加入到测试容器中
    test_unit.addTest(UCTestCase("testCreateFolder"))
    test_unit.addTest(UCTestCase("testDeleteFolder"))
    # 获取当前时间，这样便于下面的使用。
    now = time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time()))
    print(now)
    file_path = "C://Work//Result//"+"Result-"+now+".html"
    # 打开一个文件，将result写入此file中
    fp=open(file_path, 'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp, title='test result', description=u'result:')
    runner.run(test_unit)
    fp.close()
