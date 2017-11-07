# -*- coding: utf-8 -*-

'''
Created on 2016年12月3日

@author: Administrator
'''

import unittest
import time
from selenium import webdriver


ecshop = "http://172.16.3.158/ecshop/"

class Login(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()
        self.driver = driver
        return
    
    def test_login(self):
        driver = self.driver
        driver.get(ecshop)
        # 点击链接,跳转到登录页面
        driver.find_element_by_css_selector("a[href='user.php']").click()
        self.assertEqual(driver.current_url, "http://172.16.3.158/ecshop/user.php", "跳转到登录页面失败!")
        
        # 输入用户名和密码
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("tom")
        
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        
        # 点击登录
        driver.find_element_by_css_selector("input[name='submit']").click()
        
        time.sleep(5)
        self.assertEqual(driver.current_url, "http://172.16.3.158/ecshop/", "登录失败!")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()        
        