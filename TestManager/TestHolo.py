# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     TestHolo
   Author :       lenovo
   date：          2019/4/26
-------------------------------------------------
"""
import InitDriver, readConfig
from selenium import common
import time

class TestHolo(InitDriver.Driver,readConfig.Read):
    def testHole(self):
        self.r1 = readConfig.Read()
        self.driver.get(self.r1.getHoloInfo("test_url"))
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        username = self.r1.getHoloInfo("test_user")
        password  = self.r1.getHoloInfo("test_pass")
        try:
            usr = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/form/div[2]/div/div/div/input")
            usr.clear()
            usr.send_keys(username)
        except common.exceptions.NoSuchElementException as e:
            raise e
        try:
            passw = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/form/div[3]/div/div/div/input")
            passw.clear()
            time.sleep(3)
            passw.send_keys(password)
        except common.exceptions.NoSuchElementException as e:
            raise e
        try:
            self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/form/div[4]/div/button").click()
        except common.exceptions.NoSuchElementException as e:
            raise e
        try:
            self.driver.find_element_by_class_name("el-button").click()
        except common.exceptions.NoSuchElementException as e:
            raise e
        try:
            self.assertEqual('作品管理', self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div/div[1]/a").text)
        except common.exceptions.NoSuchElementException as e:
            raise e

