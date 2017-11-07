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
    
    # 点击登录
    driver.find_element_by_link_text(u"登录").click()
    
    
    # 点击"立即注册"
    driver.find_element_by_link_text(u"立即注册").click()
    
    # 默认窗口的描述符
    default_handle = driver.current_window_handle
    # 所有窗口的描述符
    all_handles = driver.window_handles
    # print "默认窗口描述符:",default_handle
    # print "所有窗口描述符:",all_handles
    
    # 切换到新窗口
    #driver.switch_to_window(window_name)
    for handle in all_handles:
        if handle != default_handle:
            driver.switch_to_window(handle)
            
    # 用户名
    driver.find_element_by_id("TANGRAM__PSP_3__userName").send_keys("Jacky")
    time.sleep(1)
    # 关闭当前浏览器窗口
    #driver.close()
    
#     print "default:",default_handle
#     print "driver.current:",driver.current_window_handle
    #切换到默认窗口
    driver.switch_to.window(default_handle)
    time.sleep(1) 
    
    driver.find_element_by_id("TANGRAM__PSP_8__userName").clear()
    driver.find_element_by_id("TANGRAM__PSP_8__userName").send_keys("abcdefg")
     
    time.sleep(3)
    driver.quit()
