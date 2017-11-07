# -*- coding: utf-8 -*-

'''
Created on 2016年12月4日

@author: Administrator
'''

from selenium import webdriver
import time



if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    driver.get("http://www.baidu.com/")
    
    driver.find_element_by_id("kw").send_keys("test")
    driver.find_element_by_id("su").click()
    
    time.sleep(1)
    # 执行JavaScript脚本,以字符串形式传参
    #driver.execute_script("window.scroll(0, 900)")
    #driver.execute_script("window.scroll(0, innerHeight)")
    driver.execute_script("window.scrollBy(0, innerHeight)")
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, innerHeight)")
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, innerHeight)")
    
    time.sleep(3)
    driver.quit()
