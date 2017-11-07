# -*- coding: utf-8 -*-

'''
Created on 2016年12月3日

@author: Administrator
'''

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time,os




if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    file_path = "file:///" + os.path.abspath("iframe_test.html")
    #print file_path
    
    # 加载本地文档
    driver.get(file_path)
    
    # 切换到内嵌框架
    # 新式方法
    #driver.switch_to.frame("test")
    #driver.switch_to.frame("testname")
    # 旧式方法
    driver.switch_to_frame("testname")
    driver.find_element_by_id("kw").send_keys("hello")
    
    
    #切换到默认框架
    driver.switch_to.default_content()
    driver.find_element_by_name("username").send_keys("jack")
    
    time.sleep(3)
    driver.quit()
    
    