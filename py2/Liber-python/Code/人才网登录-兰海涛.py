# -*- coding:utf-8 -*-
'''
Created on 2016年12月3日

@author: User
'''
import unittest
import time
from selenium import webdriver

cjol = "http://www.cjol.com"

class Login(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        self.driver = driver
        return
    
    def test_login(self):
        driver = self.driver
        driver.get(cjol)
        # 点击登录，跳转到登录界面
        driver.find_element_by_link_text(u"登录").click()
        time.sleep(5)
        self.assertEqual(driver.find_element_by_id("register_loginLayer").text, u"新用户注册", "点击登录失败！")
    
        # 输入用户名和密码
        driver.find_element_by_id("txtUserName_loginLayer").clear()
        driver.find_element_by_id("txtUserName_loginLayer").send_keys("18645555731")
        # 点击密码文本框
        driver.find_element_by_id("txtPassword_loginLayer_tip").click()
        driver.find_element_by_id("txtPassword_loginLayer").clear()
        driver.find_element_by_id("txtPassword_loginLayer").send_keys("liber130")
        
        # 取消自动登录
        driver.find_element_by_id("remember_loginLayer").click()
        
        # 点击登录
        driver.find_element_by_id("btnLogin_loginLayer").click()
        
        time.sleep(5)
        self.assertEqual(driver.find_element_by_id("a_logined_name").text, u"兰海涛", "登录失败！")
    
        driver.delete_all_cookies()
    
    
    def tearDown(self):
        self.driver.quit()
    
if __name__ == '__main__':
    unittest.main()  
    
    
    
    
    
    
    
    
    
    
    
    