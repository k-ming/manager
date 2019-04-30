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
from selenium.webdriver.common.action_chains import ActionChains
import time

class ProRobot(InitDriver.Driver, readConfig.Read):

    def proRobot(self):
        NoSuchElementException = common.exceptions.NoSuchElementException
        self.r1 = readConfig.Read()
        self.driver.get(self.r1.getRobotInfo("pro_url"))
        self.driver.implicitly_wait(10)
        username = self.r1.getRobotInfo("pro_user")
        password = self.r1.getRobotInfo("pro_pass")

        '''测试登陆'''
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
            self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[2]/span').click()
            '''Element is visible 使用xpath定位，其中用@class属性来定位，也会报这个错误（特别是class中含有复合类的定位）'''
            time.sleep(3)
        except NoSuchElementException as e:
            raise e

        '''添加机器人'''
        try:
            add_robot = self.driver.find_element_by_css_selector("div.top-head>div>button>span")
            add_robot.click()
            time.sleep(3)
            robot_no = self.driver.find_element_by_css_selector("form input[placeholder='请输入机器人编号']")
            robot_no.send_keys("test_001")
            time.sleep(1)
            robot_name = self.driver.find_element_by_css_selector("form input[placeholder='请输入机器人名称']")
            robot_name.send_keys("测试机器人001号")
            time.sleep(1)
            '''选择所在区域'''
            self.driver.find_element_by_css_selector("form input[placeholder='请选择']:nth-child(1)").click()
            time.sleep(2)
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
            self.driver.find_element_by_xpath("//body/div[5]/div[1]/div[1]/ul/li[3]").click()
            time.sleep(2)
            '''选择充电桩'''
            self.driver.find_element_by_xpath("//form/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("/html/body/div[3]").click()
            time.sleep(2)
        except NoSuchElementException as e:
            raise e






