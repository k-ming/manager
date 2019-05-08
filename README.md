# yunshen
云绅测试脚本

## selenium的css定位
#### 一、定位遇到的问题:
    1、Element is visible 使用xpath定位，其中用@class属性来定位，也会报这个错误（特别是class中含有复合类的定位）
    2、用selenium做自动化，有时候会遇到需要模拟鼠标操作才能进行的情况，比如单击、双击、点击鼠标右键、拖拽等等。而selenium给我们提供了一个类来处理这类事件——ActionChains
    3、message 消息定位，message消息通常出现时间只有几秒，所以在使用chrome浏览器调试的时候，当出现message弹窗时候，按F8暂停，copy下来xpath
#### 二、xpath、css定位比较
##### 1、css选择器匹配规则
|选择器|示例|描述|支持的css版本|
| --- |:--:|:-- |:--|
|.class|.info|选择class="info"的所有元素|1|
|#id|#firstname|选择id="firstname"的所有元素|1|
|* |*|选择所有元素|2|
|element|p|选择所有<p>元素|1|
|element,element|div,p|选择所有\<div>元素和所有\<p>元素|1|
|element element|div p|选择\<div>元素内部的所有\<p>元素|1|
|element>element|div>p|选择父元素为\<div>的所有子元素\<p>元素|2|
|element+element|div+p|选择紧接在\<div>元素之后的所有\<p>元素|2|
|[attribute]|[target]|选择带有target属性的所有元素|2|
|[attribute=vulue]|[target=_blank]|选择target="_blank"的所有元素|2|
|[attribute~=vulue]|title~=flower|选择title属性包含"flower"的所有元素|2|
|[attribute\|=vulue]|[lang\|=en]|选择lang属性值以"en"开头的所有元素|2|
|:link| a:link|选择所有未被访问的链接|1|
|:visited| a:visited|选择所有已被访问的链接|1|
|:active| a:active|选择活动链接|1|
|:hover| a:hover|选择鼠标位于其上的链接|1|
|:focus| input:focus|选择获得焦点的input元素|2|
|:first-letter| P:first-letter|选择每个\<p>元素的首字母|1|
|:first-child| p:first-child|选择属于父元素的第一个子元素的每个\<p>元素|2|
|:first-line| P:first-line| 选择每个\<p>元素的首行|1|
|:before| p:before|在每个\<p>元素的内容之前插入内容|2|
|p:after| p:after|在每个\<p>元素的内容之后插入内容|2|
|:lang(language)| p:lang(it)|选择带有以"it"开头的lang属性的每个\<p>元素|2|
|element1~element2| p~ul|选择前面有\<p>元素的每个\<ul>|3|
|[attribute^=value]| a[src^="https"]| 选择其src属性值以"https"开头的每个\<a>元素|3|
|[attrubute$=value]| a[src$=".pdf"]| 选择其src属性以".pdf"结尾的所有\<a>元素|3|
|[attrubute*=value]| a[src*="abc"]|选择其src属性包含"adc"字符串的所有\<a>元素|3|
|:first-of-type| p:first-of-type|选择属于其父元素的首个\<p>的每个\<p>元素|3|
|:last-of-type| p:last-of-type|选择属于其父元素的最后一个\<p>的每个\<p>元素|3|
|:only-of-type| p::only-of-type|选择属于其父元素唯一的\<p>的每个\<p>元素|3|
|:only-child| p::only-child|选择属于其父元素唯一子元素的\<p>元素|3|
|:nth-child(n)| p::nth-child(2)|选择属于其父元素第二子元素的\<p>元素|3|
|:nth-last-child(n)| P:nth-last-child(2)|选择属于其父元素倒数第二子元素的\<p>元素|3|
|:nth-of-type(n)| p:nth-of-type(2)|选择属于其父元素第二个\<p>的每个\<p>|3|
|:nth-last-of-type(n)| p:nth-last-of-type(2)|选择属于其父元素倒数第二个\<p>的每个\<p>|3|
|:last-child| P:last-child|选择属于其父元素最后一个子元素每个\<p>元素|3|
|:root| :root| 选择文档的根元素|3|
|:empty| p:empty|选择没有子元素的\<p>元素（包括文本节点）|3|
|:target| #news:target|选择当前活动的#news元素|3|
|:enabled| input:enabled|选择每个启动\<input>元素|3|
|:disabled| input:disabled| 选择每禁用的\<input>元素|3|
|:checked| input:checked| 选择每个被选中的\<input>元素|3|
|:not(selector)| :not(p)|选择非\<p>元素的每个元素|3|
|::selection| ::selection|选择被用户选取的元素部分|3|

#### 2、定位实例，以如下html文档为例
```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
 <head>
  <title> css locate </title>
 </head>
 <body>
  <div class="formdiv">
    <form name="fnfn">
        <input name="username" type="text"></input>
        <input name="password" type="text"></input>
        <input name="continue" type="button"></input>
        <input name="cancel" type="button"></input>
        <input value="SYS123456" name="vid" type="text">
        <input value="ks10cf6d6" name="cid" type="text">
    </form>
    <div class="subdiv">
        <a href="http://www.baidu.com" id="baiduUrl">baidu</a>
        <ul id="recordlist">
            <p>Heading</p>
            <li>Cat</li>
            <li>Dog</li>
            <li>Car</li>
            <li>Goat</li>
        </ul>
    </div>
  </div>
 </body>
</html>
```
#### 3、css选择定位实例
|cssSelector|	匹配|
|---|:---|
|css=div|\<div class="formdiv">|
|css=div.formdiv|	\<div class="formdiv">|
|css=#recordlist <br>  css=ul#recordlist| \<ul id="recordlist">|
|css=div.subdiv p|	\<p>Heading\</p>|
|css=div.subdiv>ul>p|	\<p>Heading\</p>|
|css=form+div|	\<div class="subdiv">|
|css=p+li|	\<li>Cat\</li> |
|css=p~li|	\<li>Cat\</li> 得到4个li中的第一个|
|css=form>input[name=username]|\<input name="username" type="text"></input>|
|css=input[name$=id][value^=SYS]|	\<input value="SYS123456" name="vid" type="text">|
|css=input[value*='SYS']|	\<input value="SYS123456" name="vid" type="text">|
|css=a:link|	\<a href="http://www.baidu.com">baidu\</a>|
|css=input:first-child|	\<input name="username" type="text"></input>|
|css=input:last-child|	\<input value="ks10cf6d6" name="cid" type="text">|
|css=li:nth-child(2)|	\<li>Cat\</li> 因为这个li是ul下的第二个元素，所以是child（2）|
|css=:root|	\<html>|

#### 4、XPATH和CSS定位比较，以上面的html为例
|定位方式|	XPath|	CSS|
|---|:--:|:--:|
|标签|	//div|	div|
|By id|	//div[@id='recordlist']	|div#recordlist|
|By class|	//div[@class='subdiv'] <br> //div[contains(@class,'subdiv')]|	div.subdiv
|By 属性|	//input[@name='username']|	input[name=username] <br> input[name^=user] <br> input[name$=name] <br> input[name*=erna]<br>|
|定位子元素|	//ul[@id='recordlist']/* <br> //ul/p|ul#recordlist>* <br> ul#recordlist>p|
|定位后代元素|	//div[@class='subdiv']//p|	div p|
|By index|	//li[4] 定位第四个li|	li:nth-child(5)|
|By content|	//li[contains(text(),'Goa')]|	li contains('Goa') 该方法已经废弃|
|根据子元素回溯定位父元素|//*[./a[@id='baiduUrl']] <br> //div[.//p[text()='Heading']] <br> 匹配到：\<div class="subdiv">|	？|
|根据兄弟元素定位|	//ul[preceding-sibling::a[@id='baiduUrl']]<br>//ul[preceding-sibling::a[//div[@class='subdiv']/a]]<br>都匹配到：\<ul id="recordlist">|	a+ul<br>a#baiduUrl+ul<br>匹配到：\<ul id="recordlist">|

`注意：根据兄弟元素定位时只能从上面的兄弟找下面的兄弟，如：css=p+li，写成li+p是不行的。`<br>
`可以看到，CSS定位语法比XPath更为简洁、灵活，而且CSS定位的速度还比XPath快，推荐使用CSS定位.`

## 项目讲解
#### 一 项目目录   
![项目目录](https://github.com/ming-zh/yunshen/blob/dev/TestManager/imgs/dir.jpg)  
`cases` 测试用例目录  
`config` 配置文件目录  
`imgs` readme.md文件使用的图片  
`utils`  工具类目录  
`TestManager` 根目录,InitDriver.py初始化driver类,chromedriver.exe驱动,managerTest.py 主类, QuitDriver 退出dirver类  
#### 二 文件解读
InitDriver.py初始化driver类
```python 
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
        self.driver = webdriver.Chrome('./chromedriver.exe') #初始化driver,传入驱动
        self.driver.maximize_window()

```
QuitDriver 退出dirver类   
```python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     QuitDriver
   Author :       lenovo
   date：          2019/4/26
-------------------------------------------------
"""
import InitDriver

class Quit(InitDriver.Driver): #继承初始化类,获取driver,执行quit()方法,关闭driver
    def quit(self):
        self.driver.quit()
```
managerTest.py 主类,测试用例组装与执行
```python
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
from cases import HoloLogin


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



if __name__ == '__main__':

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    '''创建测试套件, 此处一定要控制用例执行顺序,tesRobotLogin必须首先执行,否则后面的用例会报错,找不到元素,并且unittest.main()方法执行用例是按照用例字母的顺序来执行的'''
    suite = unittest.TestSuite()
    suite.addTest(TestManager('testRobotLogin'))
    suite.addTest(TestManager('testAddRobot'))
    suite.addTest(TestManager('testRobotFace'))
    suite.addTest(TestManager('testHoloLogin'))


    # 创建运行器, 并生成测试报告
    now_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    filename = "管理后台回归测试" + "_Test_" + now_time + ".html"
    fp = open(filename, 'wb+')
    runner = HTMLTestRunner_cn.HTMLTestRunner(
        stream=fp,
        title='管理后台回归测试报告',
        description='全息、机器人管理后台回归测试')
    runner.run(suite)
    fp.close()

    '''调试的时候可以用下面的方法执行,便于打印log'''
    # runer = unittest.TextTestRunner()
    # runer.run(suite)
```
utils中除了HTMLTestRunner.py,还有一个读取配置的类 readConfig.py
```python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     readConfig
   Author :       lenovo
   date：          2019/3/7
-------------------------------------------------
"""
import os
import configparser, codecs

# pd = os.path.split(os.path.realpath(__file__))[0]
'''os.path.split(os.path.realpath(__file__))[0]是获取当前文件路径,os.path.pardir是获取父目录,将他们组合起来就获取到了上层目录'''
pd = os.path.join(os.path.split(os.path.realpath(__file__))[0], os.path.pardir)
'''再组合成完整的配置文件目录'''
cp = os.path.join(pd, "config\cfg.ini") 


class Read():
    def __init__(self):
        fd = open(cp)
        data = fd.read()

        #  使用codecs模块进行文件操作及消除文件中的BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(cp, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(cp)

    def getRobotInfo(self,name):
        value = self.cf.get("ROBOT", name)
        return value

    def getHoloInfo(self,name):
        value = self.cf.get("HOLO", name)
        return value

    def getMediaInfo(self,name):
        value = self.cf.get("MEDIA", name)
        return value


# if __name__ == '__main__':
#     R1 = Read()
#     pro_url  = R1.getHoloInfo("pro_url")
#     print(pro_url)
```
配置文件 cfg.ini
```python
[HOLO]  # 全息正式测试环境地址,用户名,密码
pro_url = http://web.holo.aiyunshen.com/#/vr/workManagement
pro_user = admin
pro_pass = ys2018
test_url = http://10.11.23.138
test_user = admin
test_pass = ys2018


[ROBOT] # 机器人正式测试环境地址,用户名,密码
pro_url = http://op.robot.aiyunshen.com/info/list
pro_user = admin
pro_pass = admin123456
test_url = http://10.11.23.137
test_user = admin
test_pass = admin123456

[MEDIA]
dev_url = http://media-api.dev.rs.com

```
登陆机器人管理后台类
```python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ProRobot
   Author :       lenovo
   date：          2019/4/26
-------------------------------------------------
"""

import InitDriver
from utils import readConfig
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time

'''此处需要继承初始化driver类获得driver,后面的用例类似,只要获得到driver就可以进行测试,但是一定要注意,先执行login类打开页面,否则后面的用例无法进行'''
class RobotLogin(InitDriver.Driver, readConfig.Read): 
    '''读取配置文件中的url,用户名和密码,进行登陆操作'''
    def robotLogin(self):
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

        '''检测页面元素,如果检查的元素存在,则说明登陆成功,否则登陆失败'''
        try:
            self.assertEqual('信息管理', self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[1]/div[2]/div[1]/div/ul/div[1]/a/li/span").text)
            print('机器人管理后台登陆成功')
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
            time.sleep(2)
        except NoSuchElementException as e:
            raise e




```
