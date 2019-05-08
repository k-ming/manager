# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     VeriFace
   Author :       lenovo
   date：          2019/5/8
-------------------------------------------------
"""
import time
import unittest
import InitDriver
from selenium.common.exceptions import NoSuchElementException

class RobotFace(InitDriver.Driver, unittest.TestCase):
    def robotFace(self):
        '''----------------------------------人脸识别----------------------------------------------------------------'''
        try:
            '''人脸识别'''
            self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[3]/a/li/span').click()
            time.sleep(2)
            '''新增'''
            self.driver.find_element_by_css_selector('div.card-box>ul>li:last-child i.el-icon-plus ').click()
            time.sleep(2)
            '''点击上传'''
            self.driver.find_element_by_css_selector(
                'div.card-box>ul>li:nth-last-of-type(2)>div>div>div.top-box>div.face-img>div:nth-child(2)>div>button').click()

            '''上传文件，当html实现方式是<input type="file" name=''filename">时，可以用一下方式上传文件，否则要用AutoIT录制操作Windows窗口脚本来实现'''
            ''''''
            self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/ul/li[6]/div/div/div[1]/div[2]/div[2]/div/input').send_keys(
                'F:\yunshen\project\pic\车总.png')
            time.sleep(2)
            '''如果提示人脸重复，就不执行下面的上传过程'''
            try:
                self.driver.find_element_by_xpath('/html/body/div[2]/p')
                print(self.driver.find_element_by_xpath('/html/body/div[2]/p').text)
            except:
                '''人脸名称'''
                self.driver.find_element_by_css_selector(
                    "div.card-box>ul>li:nth-child(6) input[placeholder='请填写人脸名称']").send_keys('车总')
                time.sleep(2)
                '''欢迎语'''
                self.driver.find_element_by_css_selector(
                    "div.card-box>ul>li:nth-child(6) input[placeholder='新增问候语']").send_keys('车总,您好！')
                time.sleep(2)
                '''完成'''
                self.driver.find_element_by_css_selector(
                    'div.card-box li:nth-child(6)>div>div>div:nth-child(3)>div>span:nth-child(2)>button').click()
                print('添加人脸成功!')
                time.sleep(3)
        except NoSuchElementException as e:
            raise e
