# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     AddRobot
   Author :       lenovo
   date：          2019/5/8
-------------------------------------------------
"""
import time
import InitDriver
import unittest
from selenium.common.exceptions import NoSuchElementException


class AddRobot(InitDriver.Driver, unittest.TestCase):
    def addRobot(self):
        '''----------------------------------添加机器人----------------------------------------------------------------'''
        try:
            add_robot = self.driver.find_element_by_css_selector("div.top-head>div>button:nth-child(1)>span")
            add_robot.click()
            time.sleep(3)
            robot_no = self.driver.find_element_by_css_selector("form input[placeholder='请输入机器人编号']")
            robot_no.send_keys("test_001")
            time.sleep(1)
            self.driver.find_element_by_css_selector("form input[placeholder='请输入机器人名称']").send_keys("测试机器人001号")
            time.sleep(1)
            try:
                self.driver.find_element_by_xpath('/html/body/div[3]/p')
                print(self.driver.find_element_by_xpath('/html/body/div[3]/p').text)
            except:
                pass
            '''选择所在区域'''
            self.driver.find_element_by_css_selector("form input[placeholder='请选择']:nth-child(1)").click()
            time.sleep(1)
            try:
                self.driver.find_element_by_xpath('/html/body/div[4]/p')
                print(self.driver.find_element_by_xpath('/html/body/div[4]/p').text)
            except:
                pass
            self.driver.find_element_by_xpath("//body/div[3]/div[1]/div[1]/ul[1]/li[2]").click()
            time.sleep(2)
            '''选择楼栋'''
            self.driver.find_element_by_xpath("//form/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//body/div[4]/div[1]/div[1]/ul/li").click()
            time.sleep(2)
            '''选择楼层'''
            self.driver.find_element_by_css_selector("form div:nth-child(3) input:nth-child(1)").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//body/div[5]/div[1]/div[1]/ul/li[1]").click()
            time.sleep(2)
            '''选择充电桩'''
            self.driver.find_element_by_xpath("//form/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]").click()
            time.sleep(2)
            # 注：通过js渲染的html会隐藏已经失效的div，这样通过chrome获取的xpath不准确，一定要加上已经失效的div，否则会提示 element is not visiable
            spile = self.driver.find_element_by_xpath('//body/div[6]/div[1]/div[1]/ul/li[2]')
            spile.click()
            time.sleep(2)
            '''供应商'''
            self.driver.find_element_by_xpath('//form/div[4]/div[1]/div/div/div/div/input').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//body/div[7]/div[1]/div[1]/ul/li[2]').click()
            time.sleep(2)
            '''工作地点'''
            self.driver.find_element_by_xpath(
                '//form/div[4]/div[2]/div/div/div[1]/input[@placeholder="请输入工作点"]').send_keys('金桥商场')
            time.sleep(2)
            '''上班地点'''
            self.driver.find_element_by_xpath('//form/div[5]/div[1]/div/div/div/div/input').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//body/div[8]/div[1]/div[1]/ul/li[2]').click()
            time.sleep(2)
            '''下班地点'''
            self.driver.find_element_by_xpath('//form/div[5]/div[2]/div/div/div/div/input').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//body/div[9]/div[1]/div[1]/ul/li[2]').click()
            time.sleep(2)
            '''远程ID'''
            self.driver.find_element_by_xpath('//form/div[6]/div[1]/div/div/div[1]/input').send_keys('112233')
            time.sleep(2)
            '''远程密码'''
            self.driver.find_element_by_xpath('//form/div[6]/div[2]/div/div/div[1]/input').send_keys('223344')
            time.sleep(2)
            '''巡游点'''
            select1 = self.driver.find_element_by_xpath('//form/div[7]/div/div/div/div[1]/div/input')
            select1.click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//body/div[10]/div[1]/div[1]/ul/li[2]').click()
            time.sleep(2)
            '''添加巡游点'''
            self.driver.find_element_by_xpath('//form/div[7]/div/div/div/button').click()
            time.sleep(2)
            select1.click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//body/div[10]/div[1]/div[1]/ul/li[3]').click()
            time.sleep(2)
            '''确定'''
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div[2]/div[2]/div/div[5]/div/div/div[3]/span/button[2]/span').click()
            time.sleep(1)
            try:
                self.driver.find_element_by_xpath('/html/body/div[12]/p')
                print(self.driver.find_element_by_xpath('/html/body/div[12]/p').text)
            except:
                pass
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div[2]/div[2]/div/div[5]/div/div/div[3]/span/button[1]/span').click()
            time.sleep(1)
        except NoSuchElementException as e:
            raise e