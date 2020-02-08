# -*- coding: utf-8 -*-
"""
接口：执行所有案例
创建人：魏奇
更新人：魏奇
更新时间：2020-01-17 17:52
描述：批量执行当前文件夹下所有py文件
"""

import os

#os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
# os.getcwd() 方法用于返回当前工作目录
lst = os.listdir(os.getcwd())

# os.path.isfile()用于判断某一对象(需提供绝对路径)是否为文件
# str.endswith()判断字符串是否以指定字符或子字符串结尾
for i in lst:
    if os.path.isfile(i) and i.endswith('.py') and i.find("Run_All")==-1:  #去掉All_Run.py文件
        print(i)
        os.system(os.path.join(os.getcwd(),i))  #os.path.join拼接路径。os.system()运行
