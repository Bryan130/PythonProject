# -*- coding: utf-8 -*-

'''
Created on 2016年12月3日

@author: Administrator
'''

import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


ecshop = "http://172.16.3.158/ecshop/"

class Ecshop(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()
        self.driver = driver
        return
    
    def _login(self, driver, username, password):
        # 点击链接,跳转到登录页面
        driver.find_element_by_css_selector("a[href='user.php']").click()
        self.assertEqual(driver.current_url, "http://172.16.3.158/ecshop/user.php", "跳转到登录页面失败!")
        
        # 输入用户名和密码
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(username)
        
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        
        # 点击登录
        driver.find_element_by_css_selector("input[name='submit']").click()
        return
    
    
    def test_login(self):
        driver = self.driver
        driver.get(ecshop)
        self._login(driver, "tom", "123456")
        time.sleep(5)
        self.assertEqual(driver.current_url, "http://172.16.3.158/ecshop/", "登录失败!")
    
    def test_shopping(self):
        driver = self.driver
        driver.get(ecshop)
        
        ##################### 登录 ######################
        self._login(driver, "tom", "123456")
        time.sleep(5)
        ##################### 选购商品 #####################
        phoneType = driver.find_element_by_css_selector("a[href='category.php?id=1']")
        ActionChains(driver).move_to_element(phoneType).perform()
        driver.find_element_by_link_text(u"小型手机").click()
        
        self.assertEqual(driver.current_url, "http://172.16.3.158/ecshop/category.php?id=3", "跳转到商品搜索页面失败!")
        
        # 选择诺基亚N85,点击立即购买
        driver.find_element_by_css_selector("a[href='goods.php?id=32']").click()
        time.sleep(1)
        self.assertEqual(driver.current_url, "http://172.16.3.158/ecshop/goods.php?id=32", "跳转到商品信息页面失败!")
        
        # 选择所有配件
        driver.find_element_by_id("spec_value_158").click()
        driver.find_element_by_id("spec_value_159").click()
        driver.find_element_by_id("spec_value_157").click()
        
        # 立即购买
        driver.find_element_by_css_selector("a[href='javascript:addToCart(32)']").click()
        time.sleep(1)
        self.assertEqual(driver.current_url, "http://172.16.3.158/ecshop/flow.php?step=cart", "跳转到购物车页面失败!")
        
        # 选择数量
        # driver.find_element_by_id("goods_number_2668").clear()
        driver.find_element_by_css_selector("input[class='inputBg'][value='1']").clear()
        driver.find_element_by_css_selector("input[class='inputBg'][value='1']").send_keys("2")
        
        # 更新购物车
        #driver.find_element_by_css_selector("input[value='更新购物车']").click()
        driver.find_element_by_css_selector("input[value='更新购物车']").submit()
        time.sleep(5)
        
        # 去结算
        driver.find_element_by_css_selector("a[href='flow.php?step=checkout']").click()
        time.sleep(1)
        self.assertEqual(driver.current_url, "http://172.16.3.158/ecshop/flow.php?step=checkout", "跳转到结算页面失败!")
        
        # 修改收货人信息
        driver.find_element_by_css_selector("a[href='flow.php?step=consignee']").click()
        
        # 中国
        country = driver.find_element_by_name("country")
        country.find_element_by_css_selector("option[value='1']").click()
        # 广东省
        province = driver.find_element_by_name("province")
        province.find_element_by_css_selector("option[value='20']").click()
        # 深圳市
        city = driver.find_element_by_name("city")
        city.find_element_by_css_selector("option[value='233']").click()
        # 南山区
        district = driver.find_element_by_name("district")
        district.find_element_by_css_selector("option[value='2414']").click()
        
        driver.find_element_by_name("consignee").clear()
        driver.find_element_by_name("consignee").send_keys("Lizhichao")
        driver.find_elements_by_name("Submit")[0].click()
        
        # 配送方式:申通
        driver.find_element_by_css_selector("input[name='shipping'][value='5']").click()
        
        # 支付方式:银行汇款
        driver.find_element_by_css_selector("input[name='payment'][value='2']").click()
        
        # 精品包装
        driver.find_element_by_css_selector("input[name='pack'][value='1']").click()
        
        # 订单附言
        driver.find_element_by_name("postscript").clear()
        driver.find_element_by_name("postscript").send_keys(u"亲,请速度发货!")
        
        # 提交订单
        driver.find_element_by_css_selector("input[src='themes/default/images/bnt_subOrder.gif']").click()
        time.sleep(1)
#         msg = driver.find_element_by_tag_name("h6")
#         
#         index =  msg.text.encode("utf-8").find("您的订单已提交成功")
#         self.assertTrue(index != -1, "提交订单失败")
        source = driver.page_source
        index = source.encode("utf-8").find("您的订单已提交成功")
        self.assertTrue(index != -1, "提交订单失败")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    
    #suite.addTest(Ecshop("test_login"))        
    suite.addTest(Ecshop("test_shopping"))     
    
    unittest.TextTestRunner().run(suite)
       
        