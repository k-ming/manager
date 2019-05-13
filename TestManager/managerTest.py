# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     managerTest
   Author :       lenovo
   date：          2019/3/7
-------------------------------------------------
"""
import time, os
from utils import HTMLTestRunner_cn
import unittest
import InitDriver, QuitDriver
'''导入机器人测试用例'''
from cases import  RobotLogin,  AddRobot, RobotFace
'''导入全息测试用例'''
from cases import HoloLogin, HoloLeftMenu


class TestManager(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        InitDriver.Driver.getDriver(self)

    @classmethod
    def tearDownClass(self):
        QuitDriver.Quit.quit(self)


    def testRobotLogin(self):
        RobotLogin.RobotLogin.robotLogin(self)

    def testAddRobot(self):
        AddRobot.AddRobot.addRobot(self)

    def testRobotFace(self):
        RobotFace.RobotFace.robotFace(self)

    def testHoloLogin(self):
        HoloLogin.HoloLogin.holoLogin(self)

    def testHoloLeftMenu(self):
        HoloLeftMenu.HoloLeftMenu.holoLeftMenu(self)


if __name__ == '__main__':

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    '''创建测试套件, 此处一定要控制用例执行顺序,tesRobotLogin必须首先执行,否则后面的用例会报错,找不到元素,并且unittest.main()方法执行用例是按照用例字母的顺序来执行的'''
    suite = unittest.TestSuite()
    # suite.addTest(TestManager('testRobotLogin'))
    # suite.addTest(TestManager('testAddRobot'))
    # suite.addTest(TestManager('testRobotFace'))
    suite.addTest(TestManager('testHoloLogin'))
    # suite.addTest(TestManager('testHoloLeftMenu'))


    # 创建运行器, 并生成测试报告
    # now_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    # filename = "管理后台回归测试" + "_Test_" + now_time + ".html"
    # fp = open(filename, 'wb+')
    # runner = HTMLTestRunner_cn.HTMLTestRunner(
    #     stream=fp,
    #     title='管理后台回归测试报告',
    #     description='全息、机器人管理后台回归测试')
    # runner.run(suite)
    # fp.close()

    runer = unittest.TextTestRunner()
    runer.run(suite)

