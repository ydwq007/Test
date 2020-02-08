# -*- coding: utf-8 -*-
"""
接口：移动端登录接口- unittest
创建人：魏奇
更新人：魏奇
更新时间：2019-07-10
"""

import unittest
import sys
sys.path.append("../../Interfaces") #跨目录调用需要配置路径,接口路径
import Logins.Login as Login
sys.path.append("../../Common") #跨目录调用需要配置路径,接口路径
import DataBases, smoke,Plan
sys.path.append('../../TestDatas') #跨目录调用需要配置路径
import config
from config import test_usercenter_db

parm = smoke.Smoke(False).smoke()
url = config.test_url_chome

class Login_cases(Plan.Plan):

    def test_case01(self):
        """用户名密码均正确的情况，数据库获取"""
        print("test_case01")
        #测试参数
        #连接数据库，返回用户名数据
        db = DataBases.Mysql_links(test_usercenter_db["host"], test_usercenter_db["username"], test_usercenter_db["password"],
                                   dbname = test_usercenter_db["dbname"])
        sql = "select username from uc_members where uid = %s" % ('15634425470190000')
        db.mysqldb()
        username = db.querydata(sql)

        password = "123456"
        expected_value = True
        #调用接口
        try:
            result = Login.login_mobile(url,username[0][0], password)
            print(result)
            compare = self.assertEqual(expected_value, result[0])
            print(compare)
        # except AssertionError:
        #     print("断言失败，失败原因：期望值%s  不等于实际值 %s" % (expected_value,result))
        finally:
            print("已调用接口")


    def test_case02(self):
        """"用户名密码均正确的情况"""
        print("test_case02")
        #测试参数
        username = "gold002"
        password = "123456"
        expected_value = True
        #调用接口
        try:
            result = Login.login_mobile(url,username, password)
            print(result)
            self.assertEqual(expected_value, result[0])
        # except AssertionError:
        #     print("断言失败，失败原因：期望值%s  不等于实际值 %s" % (expected_value,result))
        finally:
            print("已调用接口")

    @unittest.skipIf(parm,"当括号内的条件为真时，跳过测试")
    def test_case03(self):
        """密码错误的情况"""
        print("test_case03")
        #测试参数
        username = "gold002"
        password = "1234561"
        expected_value = False
        #调用接口
        try:
            result = Login.login_mobile(url,username, password) #获取接口成功会失败的标记
            print(result)
            self.assertEqual(expected_value, result[0])
        # except AssertionError:
        #     print("断言失败，失败原因：期望值%s  不等于实际值 %s" % (expected_value,result))
        finally:
            print("已调用接口")

    @unittest.skipUnless(parm,"当括号内的条件为真时，执行测试")
    def test_case04(self):
        """密码为空的情况"""
        print("test_case04")
        #测试参数
        username = "gold001"
        password = ""
        expected_value = False
        #调用接口
        try:
            result = Login.login_mobile(url,username, password) #获取接口成功会失败的标记
            self.assertEqual(expected_value, result[0])
        # except AssertionError:
        #     print("断言失败，失败原因：期望值%s  不等于实际值 %s" % (expected_value,result))
        finally:
            print("已调用接口")

    @unittest.skip("直接跳过测试")
    def test_case05(self):
        """用户名为空的情况"""
        print("test_case05")
        #测试参数
        username = ""
        password = "123456"
        expected_value = False
        #调用接口
        try:
            result = Login.login_mobile(url,username, password) #获取接口成功会失败的标记
            self.assertEqual(expected_value, result[0])
        # except AssertionError:
        #     print("断言失败，失败原因：期望值%s  不等于实际值 %s" % (expected_value,result))
        finally:
            print("已调用接口")

    def test_case06(self):
        """用户名错误的情况"""
        print("test_case06")
        #测试参数
        username = "gold0011"
        password = "123456"
        expected_value = False
        #调用接口
        try:
            result = Login.login_mobile(url,username, password) #获取接口成功会失败的标记
            self.assertEqual(expected_value, result[0])
        # except AssertionError:
        #     print("断言失败，失败原因：期望值%s  不等于实际值 %s" % (expected_value,result))
        finally:
            print("已调用接口")

if __name__ == '__main__':
    unittest.main()