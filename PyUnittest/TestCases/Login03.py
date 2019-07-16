# -*- coding: utf-8 -*-
"""
接口：移动端登录接口- unittest
创建人：魏奇
更新人：魏奇
更新时间：2019-07-10
"""

import unittest
import sys
sys.path.append(r"D:\IdeaProjects\seeyon\PyUnittest\Interfaces\Logins") #跨目录调用需要配置路径,接口路径
import Login
sys.path.append(r"D:\IdeaProjects\seeyon\PyUnittest\Common") #跨目录调用需要配置路径,接口路径
import DataBases


class Login_cases():
    #初始化数据
    def __init__(self,username,password,expected_value):
        self.username = username #用户名
        self.password = password #密码
        self.expected_value = expected_value #期望值

    def test_case01(self):
        """用户名密码均正确的情况"""
        print("test_case01")
        #调用接口
        try:
            result = Login.re_login(self.username,self.password,"") #获取接口成功会失败的标记
        except AssertionError:
            print("断言失败，失败原因：期望值%s  不等于实际值 %s" % (self.expected_value,result))
        finally:
            print("已调用接口")


if __name__ == '__main__':
    #通过数据库获取登录数据
    host = "172.31.10.8" #数据库地址
    username = "usercenter" #用户名
    password = "6dfa6P3d27fe42f96f8T1268!" #密码
    dbname = "usercenter" #库名
    db = DataBases.Mysql_links(host,username,password,dbname)
    db.mysqldb()
    username = db.querydata("select username from uc_members where uid = %s" % ('-4322418878739234710'))

    # print(type(username[0][0]))
    # print(username[0][0])

    re = Login_cases(username[0][0],1234561,True)
    re.test_case01()



