# -*- coding:utf-8 -*-
'''
Created on 2016年12月6日

@author:Liber
'''
from selenium import webdriver
import time


#    人才热线登录
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.cjol.com")
# 点击登录，跳转到登录界面
driver.find_element_by_link_text(u"登录").click()
time.sleep(5)
# 输入用户名和密码
driver.find_element_by_id("txtUserName_loginLayer").clear()
driver.find_element_by_id("txtUserName_loginLayer").send_keys("liber_130@qq.com")
# 点击密码文本框
driver.find_element_by_id("txtPassword_loginLayer_tip").click()
driver.find_element_by_id("txtPassword_loginLayer").clear()
driver.find_element_by_id("txtPassword_loginLayer").send_keys("liber130")
# 取消自动登录
driver.find_element_by_id("remember_loginLayer").click()
# 点击登录
driver.find_element_by_id("btnLogin_loginLayer").click()
# 清除cookies
driver.delete_all_cookies()

# 搜索测试工程师
driver.find_element_by_id("txtKeyWords_tip").click()
driver.find_element_by_id("txtKeyWords_tip").clear()
driver.find_element_by_id("txtKeyWords").send_keys("软件测试")
driver.find_element_by_id("btnSearch").click()





time.sleep(3)

driver.quit()


