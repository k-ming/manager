# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     HoloBrands
   Author :       lenovo
   date：          2019/5/9
-------------------------------------------------
"""
import InitDriver
from utils import readConfig
from selenium.common.exceptions import NoSuchElementException
import time
import unittest

class HoloLeftMenu(InitDriver.Driver, unittest.TestCase):
    def holoLeftMenu(self):
        try:

            '''点击品牌管理菜单'''
            leftMenu = self.driver.find_element_by_xpath("//body/div/div/div/div[2]/div[1]/div/div")
            for i in range(1, 12):
                xpath = '//div['+str(i)+']/a'
                menus = ['作品管理', '场地管理', '房间管理', '品牌管理', '材质管理', '轮播管理', '品类管理', '系列管理', '订单管理', '设计师作品管理', '会员管理']
                '''校验左侧菜单是否正确'''
                self.assertEqual(leftMenu.find_element_by_xpath(xpath).text, menus[i-1])
                print(leftMenu.find_element_by_xpath(xpath).text)

        except NoSuchElementException as e:
            raise  e
