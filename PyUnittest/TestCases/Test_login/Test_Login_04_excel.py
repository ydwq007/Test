# -*- coding: utf-8 -*-
"""
接口：执行登录接口
创建人：魏奇
更新人：魏奇
更新时间：2019-12-17 20:57
描述：通过读取excel的数据，执行用例
"""

import unittest,sys
sys.path.append("../../Common") #跨目录调用需要配置路径
import Excel,smoke,Plan
parm = smoke.Smoke(False).smoke()


class Login_cases(Plan.Plan):

    def test_login_case_01(self):
        """正确用户名和正确密码登录"""

        try:
            file = Excel.open_xlsx("../../TestDatas/测试用例.xlsx")
            result = Excel.run_xlsx1(file,"login_moblie","test_login_case_01","https://testchome.seeyon.com")
            # print(result)
            self.assertEqual(True, result)
        finally:
            print("调用接口结束")

    def test_login_case_02(self):
        """正确用户名和错误密码登录"""

        try:
            file = Excel.open_xlsx("../../TestDatas/测试用例.xlsx")
            result = Excel.run_xlsx1(file,"login_moblie","test_login_case_02","https://testchome.seeyon.com")
            self.assertEqual(True, result)
        except Exception as err:
            # print(err)
            raise

    def test_login_case_03(self):
        """错误用户和正确密码"""

        try:
            file = Excel.open_xlsx("../../TestDatas/测试用例.xlsx")
            result = Excel.run_xlsx1(file,"login_moblie","test_login_case_03","https://testchome.seeyon.com")
            self.assertEqual(True, result)
        except Exception as err:
            # print(err)
            raise

    def test_login_case_04(self):
        """停用用户"""

        try:
            file = Excel.open_xlsx("../../TestDatas/测试用例.xlsx")
            result = Excel.run_xlsx1(file,"login_moblie","test_login_case_04","https://testchome.seeyon.com")
            self.assertEqual(True, result)
        except Exception as err:
            # print(err)
            raise

if __name__ == '__main__':
    unittest.main()