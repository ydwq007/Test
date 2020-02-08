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
import smoke,Plan
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

        password = "123456"
        expected_value = True
        #调用接口
        try:
            result = Login.login_mobile(url,config.usernames[0], password)
            print(result)
            compare = self.assertEqual(expected_value, result[0])
            print(compare)
        finally:
            print("已调用接口")


if __name__ == '__main__':
    unittest.main()