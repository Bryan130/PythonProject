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
    
    file_path = "file:///" + os.path.abspath("form.html")
    #print file_path
    
    # 加载本地文档
    driver.get(file_path)
    
#     # alert 警告窗口
#     driver.find_element_by_id("alert").click()
#     
#     time.sleep(1)
#     alert = driver.switch_to.alert
#     # 获取窗口的文本信息
#     print "警告信息:", alert.text
#     # 确定
#     alert.accept()
    
    # prompt 提示窗口
#     driver.find_element_by_id("prompt").click()
#     time.sleep(1)
#     
#     p = driver.switch_to.alert
#     # 向提示窗输入文本信息
#     p.send_keys("yes")
#     time.sleep(1)
#     #p.accept()
#     # 取消
#     p.dismiss()
    
    # comfirm 确认窗口
    driver.find_element_by_id("confirm").click()
    time.sleep(1)
    
    c = driver.switch_to_alert()
    time.sleep(1)
    #c.accept()
    c.dismiss()
    
    
    
    time.sleep(3)
    driver.quit()
    
    