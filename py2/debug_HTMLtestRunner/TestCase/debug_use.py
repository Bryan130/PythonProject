#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 通过testLoader方式：

import time
import unittest
import HTMLTestRunner

class TestCase1(unittest.TestCase):
    #def setUp(self):
    #def tearDown(self):
    def testCase1(self):
        pass

    def testCase2(self):
        pass

class TestCase2(unittest.TestCase):
    #def setUp(self):
    #def tearDown(self):
    def testCase1(self):
        pass

    def testCase2(self):
        self.assertEqual(2,1)

if __name__ == "__main__":
    #此用法可以同时测试多个类
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(TestCase2)
    # suite = unittest.TestSuite([suite1, suite2])
    # unittest.TextTestRunner(verbosity=1).run(suite)
    test_unit=unittest.TestSuite()
    # 将测试用例加入到测试容器中
    test_unit.addTest(TestCase1("testCase1"))
    test_unit.addTest(TestCase1("testCase2"))
    test_unit.addTest(TestCase2("testCase1"))
    test_unit.addTest(TestCase2("testCase2"))
    # 获取当前时间，这样便于下面的使用。
    now = time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time()))
    print now
    # 打开一个文件，将result写入此file中
    filePath = "C://Z_other//PythonProject//py2//debug_HTMLtestRunner//pyResult.html"
    fp = file(filePath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Python Test Report', description=u'result:')
    runner.run(test_unit)
    fp.close()
