# -*- coding: utf-8 -*-

'''
Created on 2016年12月3日

@author: Administrator
'''

import unittest
import testfunc


# 定义测试用例的类
class Maths(unittest.TestCase):
    
    
    # 类里每一个test开头的方法对应一个测试用例
    def test_add(self):
        self.assertEqual(testfunc.add(3, 5), 8, "3 + 5 != 8,用例执行失败!")
        
    def test_sub(self):
        self.assertEqual(testfunc.sub(3, 5), -2, "3 -5 != -2,用例执行失败!")
    




if __name__ == '__main__':
    unittest.main()