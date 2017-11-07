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
    
    #textarea = driver.find_element_by_id("self_intr")
    #textarea = driver.find_element("id", "self_intr")
    textarea = driver.find_element(By.ID, "self_intr")
    # Keys类定义了键盘上所有的特殊按键
    textarea.send_keys(Keys.CONTROL + "a")
    time.sleep(1)
    textarea.send_keys(Keys.CONTROL + "x")
    
   
    time.sleep(3)
    driver.quit()