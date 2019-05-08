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


class HoloLogin(InitDriver.Driver, readConfig.Read):
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
        except NoSuchElementException as e:
            raise e
        try:
            passw = self.driver.find_element_by_xpath(
                "/html/body/div/div/div/div[2]/div/div/form/div[3]/div/div/div/input")
            passw.clear()
            time.sleep(3)
            passw.send_keys(password)
        except NoSuchElementException as e:
            raise e
        try:
            self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/form/div[4]/div/button").click()
        except NoSuchElementException as e:
            raise e
        try:
            self.driver.find_element_by_class_name("el-button").click()
        except NoSuchElementException as e:
            raise e
        try:
            self.assertEqual('作品管理', self.driver.find_element_by_xpath(
                "/html/body/div[1]/div/div/div[2]/div[1]/div/div[1]/a").text)
            print('全息管理后台登陆成功')
            time.sleep(5)
        except NoSuchElementException as e:
            raise e