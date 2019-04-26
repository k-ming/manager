# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     managerTest
   Author :       lenovo
   date：          2019/3/7
-------------------------------------------------
"""
import time, os
import HTMLTestRunner
import unittest
import InitDriver, QuitDriver
import TestRobot, ProRobot, TestHolo, ProHolo


class TestManager(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        InitDriver.Driver.getDriver(self)

    @classmethod
    def tearDownClass(self):
        QuitDriver.Quit.quit(self)

    def testTestRobot(self):
        TestRobot.TestRobot.testRobot(self)

    def testProRobot(self):
        ProRobot.ProRobot.proRobot(self)

    def testTestHolo(self):
        TestHolo.TestHolo.testHole(self)

    def testProHolo(self):
        ProHolo.ProHole.proHole(self)



if __name__ == '__main__':

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    #创建测试套件
    suite = unittest.TestSuite()
    # suite.addTest(TestManager('testTestRobot'))
    suite.addTest(TestManager('testProRobot'))
    # suite.addTest(TestManager('testTestHolo'))
    suite.addTest(TestManager('testProHolo'))

    # 创建运行器
    now_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    filename = "管理后台回归测试" + "_Test_" + now_time + ".html"
    fp = open(filename, 'wb+')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='管理后台回归测试报告',
        description='全息、机器人管理后台回归测试')
    runner.run(suite)
    fp.close()


