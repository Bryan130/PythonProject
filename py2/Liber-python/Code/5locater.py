# -*- coding: utf-8 -*-

'''
Created on 2016年12月3日

@author: Administrator
'''

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
    
    #driver.find_element_by_tag_name("input").send_keys("jack")
    inputs = driver.find_elements_by_tag_name("input")
    #print "当前页面的input元素数目:", len(inputs)
    
#     for input in inputs:
#         # 获取元素的属性
#         #print input.get_attribute("type")
#         if "checkbox" == input.get_attribute("type"):
#             input.click()
    
#     chbxs = driver.find_elements_by_css_selector("input[type='checkbox']")
#     for chbx in chbxs:
#         time.sleep(1)
#         chbx.click()
    
    driver.find_element_by_xpath("/html/body/form/p[1]/input").send_keys("123456")
    #driver.find_element_by_xpath("/html/body/form/p[2]/input").send_keys("123456")
    
    
    time.sleep(3)
    driver.quit()