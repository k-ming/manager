# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     InitDriver
   Author :       lenovo
   date：          2019/4/26
-------------------------------------------------
"""
from selenium import webdriver

class Driver():
    def getDriver(self):
        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.driver.maximize_window()