#!/usr/bin/env python
# -*- coding : utf-8 -*-
# @Date      : 2017-02-28 15:19:29
# @Author  : Liber (haitao.lan@longsys.com)


from appium import webdriver
from time import sleep


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.gouhuoapp.say'
desired_caps['appActivity'] = '.view.activity.EnterChannelActivity'
desired_caps['unicodeKeyboard'] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(1)
driver.find_element_by_id('com.gouhuoapp.say:id/tv_mobile_login').click()
sleep(1)
driver.find_element_by_id('com.gouhuoapp.say:id/met_mobile').click()
sleep(1)
driver.find_element_by_id('com.gouhuoapp.say:id/met_mobile').send_keys('123456789')


# driver.find_element_by_name("1").click()

# driver.find_element_by_name("5").click()

# driver.find_element_by_name("9").click()

# driver.find_element_by_name("delete").click()

# driver.find_element_by_name("9").click()

# driver.find_element_by_name("5").click()

# driver.find_element_by_name("+").click()

# driver.find_element_by_name("6").click()

# driver.find_element_by_name("=").click()

sleep(5)
driver.quit()
