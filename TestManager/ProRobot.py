# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ProRobot
   Author :       lenovo
   date：          2019/4/26
-------------------------------------------------
"""
import InitDriver, readConfig
from selenium import common
import time

class ProRobot(InitDriver.Driver, readConfig.Read):
    def proRobot(self):
        self.r1 = readConfig.Read()
        self.driver.get(self.r1.getRobotInfo("pro_url"))
        self.driver.implicitly_wait(10)
        username = self.r1.getRobotInfo("pro_user")
        password = self.r1.getRobotInfo("pro_pass")

        try:
            user = self.driver.find_element_by_xpath("//*[@id=\"section\"]/div/div[2]/form/div[1]/div/div/input")
            user.clear()
            user.send_keys(username)
        except common.exceptions.NoSuchElementException as e:
            raise e
        try:
            passw = self.driver.find_element_by_xpath("//*[@id=\"section\"]/div/div[2]/form/div[2]/div/div/input")
            passw.clear()
            time.sleep(3)
            passw.send_keys(password)
        except common.exceptions.NoSuchElementException as e:
            raise e
        try:
            self.driver.find_element_by_class_name("el-button").click()
        except common.exceptions.NoSuchElementException as e:
            raise e
        try:
            self.assertEqual('信息管理', self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[1]/div[2]/div[1]/div/ul/div[1]/a/li/span").text)
        except common.exceptions.NoSuchElementException as e:
            raise e