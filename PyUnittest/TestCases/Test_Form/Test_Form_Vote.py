# -*- coding: utf-8 -*-
"""
接口：表单投票-未完成
创建人：魏奇
创建时间：
更新时间：
描述：
"""
import unittest,sys
sys.path.append('../../TestDatas') #跨目录调用需要配置路径，测试数据路径
from BasicDatas import usernames,password,test_url_chome
sys.path.append("../../Common") #跨目录调用需要配置路径,接口路径
import Plan
sys.path.append('../../Interfaces') #跨目录调用需要配置路径,接口路径
import Logins.Login as Login
import FormVote.Form_Vote as Form_Vote

url = test_url_chome
class Form_Vote_Cases(Plan.Plan): # 继承unittest.TestCase


    def test_01(self):
        """表单投票--不在投票时间内"""
        self.user = usernames[0]
        self.passw = password
        #调用登录接口
        self.result_login = Login.login_mobile(url,self.user, self.passw, "") #获取接口成功会失败的标记

        #调用表单投票接口
        try:
            self.result_formvote = Form_Vote.formvote(self.result_login[3]) #获取接口成功会失败的标记
            self.assertEqual(False, self.result_formvote)
        finally:
            print("已调用表单投票接口")

    def test_02(self):
        """表单投票--未登录"""
        token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjaG9tZSIsImlhdCI6MTU2NjQzNjg0Miwi" \
                "c2NvcGVzIjoicm9sZV9hY2Nlc3MiLCJleHAiOjE1NjkwMjg4NDIsInVpZCI6IjE1NjI2NTAzNzUwMTkwMDAwIn0.Gl7" \
                "7PNZsgSFF1nU4CF0HxJLcqjevUHxdPx50TUqXRCc1" #登录token

        #调用表单投票接口
        try:
            self.result_formvote = Form_Vote.formvote(token) #获取接口成功会失败的标记
            self.assertEqual(False, self.result_formvote)
        except Exception as err:
            raise err
        finally:
            print("已调用表单投票接口")

    def test_03(self):
        """表单投票--表单不存在"""
        self.user = usernames[0]
        self.passw = password
        #调用登录接口
        self.result_login = Login.login_mobile(url,self.user, self.passw, "") #获取接口成功会失败的标记
        self.login_token = self.result_login[3]
        #调用表单投票接口
        try:
            self.result_formvote = Form_Vote.formvote(self.login_token, 1111111) #获取接口成功会失败的标记
            self.assertEqual(False, self.result_formvote)
        finally:
            print("已调用表单投票接口")

    def test_04(self):
        """表单投票--正常数据"""
        self.user = usernames[0]
        self.passw = password
        #调用登录接口
        self.result_login = Login.login_mobile(url,self.user, self.passw, "") #获取接口成功会失败的标记

        #调用表单投票接口
        try:
            self.result_formvote = Form_Vote.formvote(self.result_login[3]) #获取接口成功会失败的标记
            self.assertEqual(True, self.result_formvote)
        finally:
            print("已调用表单投票接口")

if __name__ == '__main__':
    unittest.main()