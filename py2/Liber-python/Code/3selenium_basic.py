# -*- coding: utf-8 -*-

'''
Created on 2016年12月3日

@author: Administrator
'''

from selenium import webdriver
import time



baidu = "http://www.baidu.com/"
if __name__ == '__main__':
    # 创建浏览器对象,打开浏览器
    driver = webdriver.Firefox()
    
    # 窗口最大化
    driver.maximize_window()
    
#     print driver.get_window_position()
#     print driver.get_window_size()
    
    # 设置元素被定位到的最长等待时间
    driver.implicitly_wait(10)
    
    # 加载页面
    driver.get(baidu)
    
    keyword = driver.find_element_by_id("kw")
    
    # 元素属性
    # size 元素的尺寸
    # text 元素文本
    print "文本框大小: ", keyword.size
    
    print driver.find_element_by_id("setf").text
    
    # 浏览器对象属性 
    #print "浏览器名字: ", driver.name
    print "页面标题: ", driver.title
    print "页面的url: ", driver.current_url
    #print "页面的html\n: ", driver.page_source
    
    # 页面截图
    driver.get_screenshot_as_file("D:\\baidu.png")
    
    # forward() 前进  back() 后退
    driver.get("http://news.baidu.com/")
    time.sleep(1)
    driver.back()
    time.sleep(1)
    driver.forward()
    
#     # 情况文本框内容
#     keyword.clear()
#     # 模拟键盘输入
#     keyword.send_keys("hello")
#     
    
    
    time.sleep(3)
    driver.quit()
