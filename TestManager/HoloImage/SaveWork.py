# coding = utf-8

'''
读取csv文件中的名称和url,请求url,保存图片
'''
import requests
import csv
class SavePic:
    def __init__(self,dirPath,csvPath):
        r2 = self.readCsv(csvPath)
        for i in range(0,len(r2)):
            img  = requests.get(r2[i][1])
            f = open(dirPath+r2[i][0], 'ab') #保存图片是二进制形式，这里用ab
            f.write(img.content)
            print('正在保存：'+dirPath+r2[i][0])
            f.close()


    def readCsv(self, csvPath):
        r1 = csv.reader(open(csvPath, 'r', encoding='utf-8'))
        l1 = []
        for rows in r1:
            # print(rows)
            l1.append(rows)
        # print(l1)
        return l1


if __name__ == '__main__':
    s1 = SavePic('F:/yunshen/project/pic/workPics/', '/yunshen/py/yunshen/t_holoimage.csv')
