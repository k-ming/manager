# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     managerTest
   Author :       lenovo
   date：          2019/3/7
-------------------------------------------------
"""
import time, os ,sys
from selenium import common, webdriver
import HTMLTestRunner
import unittest
import readConfig
# opts = webdriver.ChromeOptions
# opts.binary_location='C:\\Users\\lenovo\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe'


class TestManager(unittest.TestCase):
    # def __init__(self):
    #     r1 = Read()
    #     print(r1.getRobotInfo("test_user"))

    def setUp(self):
        self.r1 = readConfig.Read()
        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def testPro_Robot(self):
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


    def testTest_Robot(self):
        self.driver.get(self.r1.getRobotInfo("test_url"))
        self.driver.implicitly_wait(10)
        username = self.r1.getRobotInfo("test_user")
        password = self.r1.getRobotInfo("test_pass")

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

    def testTest_holo(self):
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

    def testPro_holo(self):
        self.driver.get(self.r1.getHoloInfo("pro_url"))
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        username = self.r1.getHoloInfo("pro_user")
        password = self.r1.getHoloInfo("pro_pass")
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
            self.assertEqual('作品管理', self.driver.find_element_by_xpath( "/html/body/div[1]/div/div/div[2]/div[1]/div/div[1]/a").text)
        except common.exceptions.NoSuchElementException as e:
            raise e




if __name__ == '__main__':

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    #创建测试套件
    suite = unittest.TestSuite()
    suite.addTest(TestManager('testTest_Robot'))
    suite.addTest(TestManager('testPro_Robot'))
    suite.addTest(TestManager('testTest_holo'))
    suite.addTest(TestManager('testPro_holo'))

    # 创建运行器
    now_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    filename = "后台回归测试" + "_Test_" + now_time + ".html"
    fp = open(filename, 'wb+')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='管理后台回归测试报告',
        description='全息、机器人管理后台回归测试')
    runner.run(suite)
    fp.close()


