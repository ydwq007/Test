# -*- coding: utf-8 -*-
"""
接口：读取文本数据
创建人：魏奇
创建时间：2019-07-16

"""


import csv
import sys


# 从文件中获取数据
class FlieRead(object):

    #初始化数据
    def __init__(self, path):
        self.path = path  # 文件路径
        # self.type = type  # 文件类型

    # 读取TXT文档数据
    def txt(self, read=4):
        # 参数
        self.read = read

        # 打开文件，返回读取内容
        with open(self.path, "r") as file:
            if self.read == 1:
                self.datas = file.read().splitlines()  # 按照行界符('\r', '\r\n', \n'等)分隔读取所有内容，返list
            elif self.read == 2:
                self.datas = file.readlines()  # 一次性读取所有内容，返回list；速度比较快，但是耗内存
            elif self.read == 3:
                while True:
                    self.datas = file.readline()  # 每次读取一行读取内容，返回str；内存占用小，但速度比较慢
                    if self.datas:
                        print(self.datas)
                    else:
                        break
            else:
                self.datas = file.read()  # 读取整个文件，返回str；速度最快，但是耗内存
            return self.datas  # 返回数据

    # 读取CSV文件,也可以按照读取txt文档方式，此处采取其他方式
    def csv(self, read=4, line=1, column=1):
        """
        :param read:
        :param line:
        :param column:
        :return:
        """
        # 参数
        self.read = read
        self.line = line
        self.column = column

        # 读取CSV文件并且返回数据
        self.datas = []
        self.file = csv.reader(open(self.path, "r"))  # 读取CSV文件
        if self.read == 1:  # 从指定行开始读取
            for i, j in enumerate(self.file):
                if i >= self.line-1:
                    self.datas.append(j)
        elif self.read == 2:  # 读取指定行
            for i, j in enumerate(self.file):
                if i == self.line-1:
                    self.datas.append(j)
        elif self.read == 3:  # 读取指定列
            for i in self.file:
                self.datas.append(i[self.column-1])
        else:  # 读取所有数据
            for i in self.file:
                self.datas.append(i)
        return self.datas

    # 读取xlsx文件
    def xlsx(self, read=4, line=2, column=1):
        """
        :param read:
        :param line:
        :param column:
        :return:
        """
        # 参数
        self.read = read
        self.line = line
        self.column = column

        # 读取xlsx文件并且返回数据
        self.datas = []
        self.file = csv.reader(open(self.path, "r"))  # 读取xlsx文件
        if self.read == 1:  # 从指定行开始读取
            for i, j in enumerate(self.file):
                if i >= self.line-1:
                    self.datas.append(j)
        elif self.read == 2:  # 读取指定行
            for i, j in enumerate(self.file):
                if i == self.line-1:
                    self.datas.append(j)
        elif self.read == 3:  # 读取指定列
            for i in self.file:
                self.datas.append(i[self.column-1])
        else:  # 读取所有数据
            for i in self.file:
                self.datas.append(i)
        return self.datas


if __name__ == "__main__":
    # path1 = r"..\TestDatas\文本数据.txt"
    # path2 = r"..\TestDatas\客户数据表.csv"
    path1 = "../TestDatas/文本数据.txt"
    path2 = "../TestDatas/客户数据表.csv"
    path3 = "../TestDatas/接口测试用例.csv"
    re1 = FlieRead(path1)
    re2 = FlieRead(path2)
    re3 = FlieRead(path3)
    # context = re1.txt(3)
    context = re3.xlsx(read=4)
    print(context)