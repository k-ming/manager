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

pd = os.path.split(os.path.realpath(__file__))[0]
cp = os.path.join(pd, "cfg.ini")


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