# -*- coding: utf-8 -*-

'''
Created on 2016年12月3日

@author: Administrator
'''

from selenium import webdriver
import time



baidu = "http://www.baidu.com/"
if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    
    driver.get(baidu)
    
    
    # find_element_by_xxx  定位一个页面元素,返回页面元素
    # find_elements_by_xxx 定位一组页面元素,返回列表
    
    # 根据id定位元素 
    # driver.find_element_by_id("kw").send_keys(u"软件测试")
    
    # 根据name定位元素 
    #driver.find_element_by_name("wd").send_keys(u"软件测试")
   
    # 根据class定位元素
    s_ipts = driver.find_elements_by_class_name("s_ipt")
#     print s_ipts
#     print len(s_ipts)
    #s_ipts[0].send_keys(u"软件测试")
    
    # css选择器
    #driver.find_element_by_css_selector("input[maxlength='255']").send_keys("test")
    #driver.find_element_by_css_selector("input[id='kw']").send_keys("test")
    #driver.find_element_by_css_selector("input[name='wd'][id='kw']").send_keys("test")
    
    #driver.find_element_by_css_selector("input#kw").send_keys("test")
    
    # parent > son 子元素
    #driver.find_element_by_css_selector("form#form > span > input#kw").send_keys("test")
    # 祖先   后代
    #driver.find_element_by_css_selector("form#form  span  input#kw").send_keys("test")
    #driver.find_element_by_css_selector("form#form  input#kw").send_keys("test")
    
    # xpath
    #driver.find_element_by_xpath("//*[@id='kw']").send_keys("test")
    #driver.find_element_by_xpath("//input[@id='kw']").send_keys("test")
    #driver.find_element_by_xpath("//form[@id='form']/span[1]/input[1]").send_keys("test")
    #driver.find_element_by_xpath("//form[@id='form']/span[1]/input[@id='kw']").send_keys("test")
    #driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/span[1]/input").send_keys("test")
    
    # 链接定位方式
    # 根据链接文字
    #driver.find_element_by_link_text(u"关于百度").click()
    # 根据部分链接文字
    driver.find_element_by_partial_link_text(u"关于百").click()
    
    
    time.sleep(3)
    driver.quit()