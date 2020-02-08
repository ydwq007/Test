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
import Excel,smoke,Plan,Excel_Manage
parm = smoke.Smoke(False).smoke()
sys.path.append("../../TestDatas")
import config


Test_Url = config.test_url_chome
filepath = "../../TestDatas/接口测试用例.xlsx"
resheetname = "login_moblie"
mdsheetname = "normal_order_create"

class Login_cases(Plan.Plan):

    def test_login_case_01(self):
        """正确用户名和正确密码登录"""

        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"test_login_case_01",Test_Url)
            # print(result)
            self.assertEqual(True, result[0])
            login_token = result[1]["data"]["token"]["access_token"]

            # #更新数据
            # value = {
            #     "Content-Type": "application/json",
            #     "Authorization":"Bearer %s" % login_token
            # }
            # mdvalue = "%s" % value
            # excel_xl = Excel_Manage.excelprocess_xl()
            # excel_xl.write_excel_xls_modify(filepath,16,5,mdvalue,sheet_name=mdsheetname,style=3,original_row=4)

        except Exception as err:
            # print(err)
            raise
        finally:
            print("调用接口结束")

    def test_login_case_02(self):
        """正确用户名和错误密码登录"""

        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"test_login_case_02",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            # print(err)
            raise

    def test_login_case_03(self):
        """错误用户和正确密码"""

        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"test_login_case_03",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            # print(err)
            raise

    def test_login_case_04(self):
        """停用用户"""

        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"test_login_case_04",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            # print(err)
            raise

if __name__ == '__main__':
    unittest.main()