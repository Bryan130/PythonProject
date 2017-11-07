# -*- coding:utf-8 -*-
'''
Created on 2016.11.17

@author: haitao.lan
'''

from selenium import webdriver
from time import *
from selenium.webdriver import ActionChains
# 打开浏览器
driver = webdriver.Chrome()
sleep(2)
# 输入网址
driver.get("http://www.baidu.com")
sleep(1)

# 一.正确的用户名和密码登录
print ("开始执行用例一")
# 1.定位‘登录’并点击
driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()

sleep(3)
# 2.定位‘用户名’文本框
driver.find_element_by_id("TANGRAM__PSP_8__userName").clear()
# 3.输入用户名
driver.find_element_by_id("TANGRAM__PSP_8__userName").send_keys("18645555731")
# 4.定位‘密码’文本框
driver.find_element_by_id("TANGRAM__PSP_8__password").clear()
# 5.输入密码
driver.find_element_by_id("TANGRAM__PSP_8__password").send_keys("lanhaitao130")
sleep(15)
# 6.点击‘下次自动登录’
driver.find_element_by_id("TANGRAM__PSP_8__memberPass").click()
# 7.点击‘登录’
driver.find_element_by_id("TANGRAM__PSP_8__submit").click()
sleep(5)
# 8.获取‘用户名’文本值
TX1=driver.find_element_by_xpath('//*[@id="s_username_top"]/span').text
# 9.打印获取的文本值
print ('打印元素内容 :', TX1)
print ('测试用例一执行结果：')
# 10.验证是否登录成功
if TX1 == "海涛130v":
    print ("登录成功")
else:
    print ("登录失败")
sleep(3)
## 11.定位‘用户名’
# username = driver.find_element_by_xpath('//*[@id="s_username_top"]/span')
# sleep(5)
# # # 12.鼠标悬浮在‘用户名’上
# # ActionChains(driver).move_to_element(username).perform()
# # sleep(5)
# # # 13.定位‘退出’并点击
# # driver.find_element_by_xpath('//*[@id="s_user_name_menu"]/div/a[5]').click()
# # sleep(5)
# # # 14.定位‘确定’并点击
# # driver.find_element_by_xpath('//*[@id="tip_con_wrap"]/div[3]/a[3]').click()
# # sleep(5)
driver.quit()
sleep(2)
print ('关闭浏览器')
print ()
  
  
# 二.用户名密码均为空登录
print ("开始执行用例二")
driver = webdriver.Chrome()
sleep(3)
driver.get("http://www.baidu.com")
# 1.定位‘登录’并点击
driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
sleep(3)
# 2.点击‘登录’
driver.find_element_by_id("TANGRAM__PSP_8__submit").click()
sleep(5)
# 3.获取‘提示信息’文本值
TX2=driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_8__error"]').text
# 4.打印获取的文本值
print ('打印元素内容 :', TX2)
print ('测试用例二执行结果：')
sleep(4)
# 5.验证用例是否执行通过
if TX2 == "请您填写手机/邮箱/用户名":
    print ("pass")
else:
    print ("false")
sleep(5)
# 6.退出浏览器
driver.quit()
print ('关闭浏览器')
sleep(3)
print ()

# 三.用户名输入正确，密码为空登录
print ('开始执行用例三')
# 打开浏览器
driver = webdriver.Chrome()
sleep(5)
# 输入网址
driver.get("http://www.baidu.com")
# 1.定位‘登录’并点击
driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
sleep(5)
# 2.定位‘用户名’文本框
driver.find_element_by_id("TANGRAM__PSP_8__userName").clear()
# 3.输入用户名
driver.find_element_by_id("TANGRAM__PSP_8__userName").send_keys("18645555731")

sleep(3)
# 4.点击‘登录’
driver.find_element_by_id("TANGRAM__PSP_8__submit").click()
sleep(5)
# 5.获取‘提示信息’文本值
TX3=driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_8__error"]').text
# 4.打印获取的文本值
print ('打印元素内容 :', TX3)
print ('测试用例三执行结果：')
sleep(4)
# 5.验证用例是否执行通过
if TX3 == "请您填写密码":
    print ("pass")
else:
    print ("false")
sleep(5)
# 6.退出浏览器
driver.quit()
print ('关闭浏览器')
print ()
# 四.用户名输入正确，密码为空登录
print ('开始执行用例四')
# 打开浏览器
driver = webdriver.Chrome()
sleep(5)
# 输入网址
driver.get("http://www.baidu.com")
# 1.定位‘登录’并点击
driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
sleep(5)
# 2.定位‘用户名’文本框
driver.find_element_by_id("TANGRAM__PSP_8__userName").clear()
# 3.输入用户名
driver.find_element_by_id("TANGRAM__PSP_8__userName").send_keys("18645555731000")
# 4.定位‘密码’文本框
driver.find_element_by_id("TANGRAM__PSP_8__password").clear()
# 5.输入密码
driver.find_element_by_id("TANGRAM__PSP_8__password").send_keys("lanhaitao130")
sleep(10)
# 6.点击‘登录’
driver.find_element_by_id("TANGRAM__PSP_8__submit").click()
sleep(5)
# 7.获取‘提示信息’文本值
TX4=driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_8__error"]').text
# 8.打印获取的文本值
print ('打印元素内容 :', TX4)
print ('测试用例四执行结果：')
sleep(4)
# 9.验证用例是否执行通过
if TX4 == "您输入的帐号不存在，可查看帮助或立即注册":
    print ("pass")
else:
    print ("false")
sleep(5)
# 10.退出浏览器
driver.quit()
print ('关闭浏览器')
print ()

# 五.用户名输入正确，错误的密码登录
print ('开始执行用例五')
# 打开浏览器
driver = webdriver.Chrome()
sleep(5)
# 输入网址
driver.get("http://www.baidu.com")
# 1.定位‘登录’并点击
driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
sleep(5)
# 2.定位‘用户名’文本框
driver.find_element_by_id("TANGRAM__PSP_8__userName").clear()
# 3.输入用户名
driver.find_element_by_id("TANGRAM__PSP_8__userName").send_keys("18645555731")
# 4.定位‘密码’文本框
driver.find_element_by_id("TANGRAM__PSP_8__password").clear()
# 5.输入密码
driver.find_element_by_id("TANGRAM__PSP_8__password").send_keys("lanhaitao0")
sleep(15)
# 6.点击‘登录’
driver.find_element_by_id("TANGRAM__PSP_8__submit").click()
sleep(5)
# 7.获取‘提示信息’文本值
TX5=driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_8__error"]').text
# 8.打印获取的文本值
print ('打印元素内容 :', TX5)
print ('测试用例五执行结果：')
sleep(4)
# 9.验证用例是否执行通过
if TX5 == "密码错误，可以试试短信登录 ,或者找回密码":
    print ("pass")
else:
    print ("false")
sleep(5)
# 10.退出浏览器
driver.quit()
print ('关闭浏览器')










