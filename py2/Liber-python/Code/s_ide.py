# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://change-this-to-the-site-you-are-testing/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled(self):
        driver = self.driver
        driver.get("http://172.16.3.158/ecshop/")
        self.assertEqual(u"ECSHOP演示站 - Powered by ECShop", driver.title)
        driver.find_element_by_link_text(u"请登录").click()
        self.assertEqual(u"用户中心_ECSHOP演示站 - Powered by ECShop", driver.title)
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("tom")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_name("submit").click()
        self.assertEqual(u"系统提示_ECSHOP演示站 - Powered by ECShop", driver.title)
        time.sleep(5)
        self.assertEqual(u"ECSHOP演示站 - Powered by ECShop", driver.title)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()