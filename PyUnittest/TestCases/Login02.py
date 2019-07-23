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


# def run_login(username,password,expected_value):
#     try:
#         result = Login1.re_login(username,password,"") #获取接口成功会失败的标记
#         assertEqual(expected_value, result)
#     except AssertionError:
#         print("断言失败，失败原因：期望值%s  不等于实际值 %s" % (expected_value,result))
#     except TypeError:
#         print("验证码次数超过最多限制,SendCode接口报错")
#     except IndexError:
#         print("序列中没有此索引(index),SendCode接口报错")
#     finally:
#         print("已调用接口")

class Login_cases(unittest.TestCase): # 继承unittest.TestCase

    @classmethod
    def setUpClass(cls):
        #所有case执行之前的前置，测试用例需要登录web，可以先实例化浏览器
        print("\n","脚本执行开始")

    @classmethod
    def tearDownClass(cls):
        #所有case执行之后的后置，如关闭数据库连接。关闭浏览器。
        print("脚本执行结束","\n")

    def setUp(self):
        # # 每个测试用例执行之前做操作
        print("\n","案例开始执行")

    def tearDown(self):
        # 每个测试用例执行之后做操作
        print("案例完成执行","\n")

    def test_case01_1(self):
        """用户名密码均正确的情况，数据库获取"""
        print("test_case01_1")
        #测试参数
        #连接数据库，返回用户名数据
        db = DataBases.Mysql_links(test_usercenter_db["host"],test_usercenter_db["username"],test_usercenter_db["password"],
                                   dbname = test_usercenter_db["dbname"])
        sql = "select username from uc_members where uid = %s" % ('-4322418878739234710')
        db.mysqldb()
        username = db.querydata(sql)

        password = "123456"
        expected_value = True
        #调用接口
        try:
            result = Login.re_login(username[0][0],password,"") #获取接口成功会失败的标记
            self.assertEqual(expected_value, result)
        # except AssertionError:
        #     print("断言失败，失败原因：期望值%s  不等于实际值 %s" % (expected_value,result))
        finally:
            print("已调用接口")

    def test_case01(self):
        """"用户名密码均正确的情况"""
        print("test_case01")
        #测试参数
        username = "gold001"
        password = "1234561"
        expected_value = True
        #调用接口
        try:
            result = Login.re_login(username,password,"") #获取接口成功会失败的标记
            self.assertEqual(expected_value, result)
        # except AssertionError:
        #     print("断言失败，失败原因：期望值%s  不等于实际值 %s" % (expected_value,result))
        finally:
            print("已调用接口")

    def test_case02(self):
        """密码错误的情况"""
        print("test_case02")
        #测试参数
        username = "gold001"
        password = "1234561"
        expected_value = False
        #调用接口
        try:
            result = Login.re_login(username,password,"") #获取接口成功会失败的标记
            self.assertEqual(expected_value, result)
        # except AssertionError:
        #     print("断言失败，失败原因：期望值%s  不等于实际值 %s" % (expected_value,result))
        finally:
            print("已调用接口")

    def test_case03(self):
        """密码为空的情况"""
        print("test_case03")
        #测试参数
        username = "gold001"
        password = ""
        expected_value = False
        #调用接口
        try:
            result = Login.re_login(username,password,"") #获取接口成功会失败的标记
            self.assertEqual(expected_value, result)
        # except AssertionError:
        #     print("断言失败，失败原因：期望值%s  不等于实际值 %s" % (expected_value,result))
        finally:
            print("已调用接口")

    def test_case04(self):
        """用户名为空的情况"""
        print("test_case04")
        #测试参数
        username = ""
        password = "123456"
        expected_value = False
        #调用接口
        try:
            result = Login.re_login(username,password,"") #获取接口成功会失败的标记
            self.assertEqual(expected_value, result)
        # except AssertionError:
        #     print("断言失败，失败原因：期望值%s  不等于实际值 %s" % (expected_value,result))
        finally:
            print("已调用接口")

    def test_case05(self):
        """用户名错误的情况"""
        print("test_case05")
        #测试参数
        username = "gold0011"
        password = "123456"
        expected_value = False
        #调用接口
        try:
            result = Login.re_login(username,password,"") #获取接口成功会失败的标记
            self.assertEqual(expected_value, result)
        # except AssertionError:
        #     print("断言失败，失败原因：期望值%s  不等于实际值 %s" % (expected_value,result))
        finally:
            print("已调用接口")

if __name__ == '__main__':
    unittest.main()