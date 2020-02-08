# -*- coding: utf-8 -*-
"""
接口：0元订单
创建人：魏奇
更新人：魏奇
更新时间：2020-02-07 16:01
描述：
"""

import unittest,sys,requests,json
sys.path.append("../../Commom")
import Excel,Plan,Excel_Manage
sys.path.append("../../TestDatas")
import config

Test_Url = config.test_url_mall
filepath = config.filepath
resheetname = "zero_order_create"
loginsheet = "login_moblie"
loginurl = config.test_url_chome

class Nomal_Order_Create(Plan.Plan):

    # 登录
    file = Excel.open_xlsx(filepath)

    # 含B类账号登录
    login_result1 = Excel.run_xlsx1(file,loginsheet,"test_login_case_01",loginurl)
    login_token1 = login_result1[1]["data"]["token"]["access_token"]
    #更新数据
    value1 = """{
        "Content-Type": "application/json",
        "Authorization":"Bearer %s" 
    }""" % login_token1
    mdvalue1 = "%s" % value1

    #纯A类账号登录
    login_url = "%s/portal.php" % loginurl
    login_data = {
        "m":"userMobileLogin",
        "a":"login",
        "username":"15982280117",
        "password":"123456",
        "account_type":"1"
    }
    login_request = requests.post(url=login_url,data=json.dumps(login_data),headers=config.headers,verify=False)
    login_result2= json.loads(login_request.text)
    print(login_result2)
    login_token2 = login_result2["data"]["token"]["access_token"]
    #更新数据
    value2 = """{
        "Content-Type": "application/json",
        "Authorization":"Bearer %s" 
    }""" % login_token2
    mdvalue2 = "%s" % value2

    excel_xl = Excel_Manage.excelprocess_xl()
    # 修改第5行到17行的第4列的值
    excel_xl.write_excel_xls_modify(filepath,17,5,mdvalue1,sheet_name=resheetname,style=3,original_row=5)
    excel_xl.write_excel_xls_modify(filepath,4,5,mdvalue1,sheet_name=resheetname,style=1)


    def test_zero_order_create_case_01(self):
        """正常订单数据（含B类账号）"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"zero_order_create_case_01",Test_Url)
            self.assertEqual(True, result[0])
            # print(result)
            nomal_order_id = result[1]["data"]["data"]["order_id"]
            return nomal_order_id #返回创建成功的普通订单id
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

if __name__ == "__main__":
    unittest.main()
