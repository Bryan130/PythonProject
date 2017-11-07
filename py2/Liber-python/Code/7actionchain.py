# -*- coding: utf-8 -*-

'''
Created on 2016年12月4日

@author: Administrator
'''

# -*- coding: utf-8 -*-

'''
Created on 2016年12月3日

@author: Administrator
'''

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time,os


ecshop = "http://172.16.3.158/ecshop/"

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    driver.get(ecshop)
    
    # 创建ActionChains对象,参数是浏览器对象
    ac = ActionChains(driver)
    type = driver.find_element_by_link_text(u"手机类型")
    # 把事件添加到ac内部的事件队列
    #ac.context_click(on_element) 鼠标右键点击
    #ac.double_click(on_element)  鼠标双击
    
    # 移动鼠标指针到某个元素上
    ac.move_to_element(type)
    # 执行所有的事件(按照添加的顺序执行)
    ac.perform()
    
    #ActionChains(driver).move_to_element(driver.find_element_by_link_text(u"手机类型")).perform()
    
    # 点击小型手机链接
    driver.find_element_by_css_selector("a[href='category.php?id=3']").click()
    
    
    
    
    time.sleep(3)
    driver.quit()