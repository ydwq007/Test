# -*- coding: utf-8 -*-
"""
接口：移动端登录接口- unittest
创建人：魏奇
更新人：魏奇
更新时间：2019-07-10
"""

import unittest
import sys
sys.path.append(r"\PyUnittest\Interfaces\Logins") #跨目录调用需要配置路径,接口路径
import Login
sys.path.append(r"\PyUnittest\Common") #跨目录调用需要配置路径,接口路径
import DataBases,file
sys.path.append(r'\PyUnittest\TestDatas') #跨目录调用需要配置路径
from config import test_usercenter_db

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
    #连接数据库，返回用户名数据
    db = DataBases.Mysql_links(test_usercenter_db["host"],test_usercenter_db["username"],test_usercenter_db["password"],
                               dbname = test_usercenter_db["dbname"])
    sql = "select username from uc_members where uid = %s" % ('-4322418878739234710')
    db.mysqldb()
    username = db.querydata(sql)

    re = Login_cases(username[0][0],123456,True)
    re.test_case01()

    path1 = r"\PyUnittest\TestDatas\文本数据.txt"
    path2 = r"\PyUnittest\TestDatas\客户数据表.csv"
    re1 = file.FlieRead(path1)
    re2 = file.FlieRead(path2)
    # context = re1.txt(3)
    context = re2.csv(line=2,read=3)
    print(context)



