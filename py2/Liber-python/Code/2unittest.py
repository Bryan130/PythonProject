# -*- coding: utf-8 -*-

'''
Created on 2016年12月3日

@author: Administrator
'''

import unittest
import testclass


class Foo(unittest.TestCase):

    # 执行每个测试用例函数之前会先执行setUp,初始化执行环境
    def setUp(self):
        #print "setUp..."
        self.m = testclass.Maths()


    def test_add(self):
        m = self.m
        ret = m.add(3, 5)
        self.assertEqual(ret, 8, "3 + 5 != 8")

    def test_sub(self):
        m = self.m
        ret = m.sub(3, 5)
        self.assertEqual(ret, -2, "3 - 5 != -2")

    def test_mul(self):
        m = self.m
        ret = m.mul(3, 5)
        self.assertEqual(ret, 15, "3 * 5 != 15")

    # 执行完每个测试用例函数后,会执行tearDown函数,清理执行环境
    def tearDown(self):
        del self.m


if __name__ == '__main__':
    unittest.main()
    # 创建测试套件
    ts = unittest.TestSuite()

    # 把测试用例添加到测试套件
    ts.addTest(Foo('test_add'))
    ts.addTest(Foo('test_mul'))

    # 创建可以执行测试套件的对象
    runner = unittest.TextTestRunner()
    # 执行测试套件
    runner.run(ts)
    runner.run(Foo("test_add"))

