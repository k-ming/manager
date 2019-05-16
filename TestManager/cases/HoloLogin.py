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
            '''输入用户名和密码'''
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

            time.sleep(2)

            '''校验用户登陆成功'''
            admin =self.driver.find_element_by_xpath('//body/div[1]/div/div/div[1]/div[2]/ul/li/div').text

            self.assertEqual(admin, 'admin')


        except NoSuchElementException as e:
            raise e

















