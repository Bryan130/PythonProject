#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os
import time
import unittest
import HTMLTestRunner

result_path = "./result"
dir_list = ["/acc", "/dev"]
base_dir = "./TestCase"

def Create_Suite():
    """

    :return:
    """
    testunit = unittest.TestSuite()
    # discover方法定义
    for item in dir_list:
        dirs = base_dir + item
        print dirs
        discover = unittest.defaultTestLoader.discover(dirs, pattern="test_*.py", top_level_dir=None)
        print 111

        # discover 方法筛选出来的用例，循环添加到测试套件中
        for test_suite in discover:
            for test_case in test_suite:
                testunit.addTests(test_case)

    return testunit


if __name__ == "__main__":
    # 所有的用例集合
    all_test_cases = Create_Suite()

    # 获取系统当前时间
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 定义单个测试报告的存放路径，支持相对路径
    result_paths = result_path + "\\" + day

    # 若已经存在以当天日期为名称的文件夹的情况，则直接将测试报告放到这个文件夹之下
    if os.path.exists(result_paths):
        filename = result_paths + "\\" + now + "_result.html"
        # 以写文本文件或写二进制文件的模式打开测试报告文件
        fp = file(filename, 'wb')
        # 定义测试报告
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'Backend-V1.0.0-自动化测试报告', description=u'用例执行情况如下：')
        # 运行测试用例
        runner.run(all_test_cases)
        # 关闭报告文件
        fp.close()
    else:
        # 不存在以当天日期为名称的文件夹的情况，则建立一个以当天日期为名称的文件夹
        os.mkdir(result_paths)
        # 以写文本文件或写二进制文件的模式打开测试报告文件
        filename = result_paths + r"\\" + now + "_result.html"
        fp = file(filename, 'wb')
        # 定义测试报告
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'用例执行情况：')
        # 运行测试用例
        runner.run(all_test_cases)
        # 关闭报告文件
        fp.close()
