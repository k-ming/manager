# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     QuitDriver
   Author :       lenovo
   date：          2019/4/26
-------------------------------------------------
"""
import InitDriver

class Quit(InitDriver.Driver):
    def quit(self):
        self.driver.quit()