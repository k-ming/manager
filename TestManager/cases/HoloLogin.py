# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ProHolo
   Author :       lenovo
   date：          2019/4/26
-------------------------------------------------
"""
import InitDriver
from utils import readConfig
from selenium.common.exceptions import NoSuchElementException
import time
import unittest


class HoloLogin(InitDriver.Driver, readConfig.Read, unittest.TestCase):
    def holoLogin(self):
        self.r1=readConfig.Read()
        self.driver.get(self.r1.getHoloInfo("pro_url"))
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        username = self.r1.getHoloInfo("pro_user")
        password = self.r1.getHoloInfo("pro_pass")
        try:
            usr = self.driver.find_element_by_xpath(
                "/html/body/div/div/div/div[2]/div/div/form/div[2]/div/div/div/input")
            usr.clear()
            usr.send_keys(username)

            passw = self.driver.find_element_by_xpath(
                "/html/body/div/div/div/div[2]/div/div/form/div[3]/div/div/div/input")
            passw.clear()
            time.sleep(3)
            passw.send_keys(password)

            self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/form/div[4]/div/button").click()

            self.driver.find_element_by_class_name("el-button").click()

            # self.assertEqual('全息投影后台管理系统', self.driver.find_element_by_css_selector(
            #         "body > div > div > div > div.header > div.headerLogo > p").text)
            # print(self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]').location)
            print(self.driver.find_element_by_class_name('user-info-photo').location)
            time.sleep(2)

        except NoSuchElementException as e:
            raise e

















