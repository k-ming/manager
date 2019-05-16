# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ProRobot
   Author :       lenovo
   date：          2019/4/26
-------------------------------------------------
"""

import InitDriver
from utils import readConfig
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest


class RobotLogin(InitDriver.Driver, readConfig.Read, unittest.TestCase):

    def robotLogin(self):
        self.r1 = readConfig.Read()
        self.driver.get(self.r1.getRobotInfo("pro_url"))
        self.driver.implicitly_wait(10)
        username = self.r1.getRobotInfo("pro_user")
        password = self.r1.getRobotInfo("pro_pass")

        # '''测试登陆'''
        try:
            user = self.driver.find_element_by_xpath("//*[@id=\"section\"]/div/div[2]/form/div[1]/div/div/input")
            user.clear()
            user.send_keys(username)
        except NoSuchElementException as e:
            raise e
        try:
            passw = self.driver.find_element_by_xpath("//*[@id=\"section\"]/div/div[2]/form/div[2]/div/div/input")
            passw.clear()
            time.sleep(3)
            passw.send_keys(password)
        except NoSuchElementException as e:
            raise e
        try:
            self.driver.find_element_by_class_name("el-button").click()
        except NoSuchElementException as e:
            raise e

        '''检测页面元素'''
        try:
            self.assertEqual('信息管理', self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[1]/div[2]/div[1]/div/ul/div[1]/a/li/span").text)
            print('机器人管理后台登陆成功')
        except NoSuchElementException as e:
            raise e

        '''选择商场'''
        try:
            choose = self.driver.find_element_by_xpath('//input[@placeholder="请选择商场"]')
            ActionChains(self.driver).click(choose).perform()
            time.sleep(3)
        except NoSuchElementException as e:
            raise e

        try:
            # self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[2]/span').click()
            '''Element is visible 使用xpath定位，其中用@class属性来定位，也会报这个错误（特别是class中含有复合类的定位）'''

            eles = self.driver.find_elements_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li')
            for i in eles:
                if (i.text == u'爱琴海购物公园'):
                    print(i.text)
                    i.click()
                    time.sleep(2)
                else: pass


        except NoSuchElementException as e:
            raise e



