# -*- coding: utf-8 -*-
"""
接口：普通订单的创建
创建人：魏奇
更新人：魏奇
更新时间：2020-01-08 9:23
描述：
"""

import unittest,sys,requests,json
sys.path.append("../../Commom")
import Excel,Plan,Excel_Manage
sys.path.append("../../TestDatas")
import config

Test_Url = config.test_url_mall
filepath = config.filepath
resheetname = "normal_order_create"
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


    def test_nomal_order_create_case_01(self):
            """正常订单数据（含B类账号）"""
            try:
                file = Excel.open_xlsx(filepath)
                result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_01",Test_Url)
                self.assertEqual(True, result[0])
                # print(result)
                nomal_order_id = result[1]["data"]["data"]["order_id"]
                return nomal_order_id #返回创建成功的普通订单id
            except Exception as err:
                raise
            finally:
                print("调用接口结束")

    def test_nomal_order_create_case_02(self):
        """用户未登录"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_02",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_create_case_03(self):
        """token失效"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_03",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_create_case04(self):
        """user_id-非必填"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_04",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_create_case_05(self):
        """goods_sku_list-必填"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_05",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_create_case_06(self):
        """goods_sku_list-商品不存在"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_06",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_create_case_07(self):
        """buyer_org_id-必填"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_07",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_create_case_08(self):
        """buyer_org_id-客户单位不存在"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_08",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_create_case_09(self):
        """buyer_org_id-客户单位不匹配"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_09",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_create_case_10(self):
        """service_org_id-必填"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_10",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_create_case_11(self):
        """service_org_id-经销商不存在"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_11",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_create_case_12(self):
        """service_org_id-经销商不匹配"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_12",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_create_case_13(self):
        """company_name-必填"""
        # 有分歧，待确认
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_13",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_create_case_14(self):
        """contact_name-非必填"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_14",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_create_case_15(self):
        """contact_phone-必填"""
        # 有分歧，待确认
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_15",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_create_case_16(self):
        """正常订单数据（纯A类账号）"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_create_case_16",Test_Url)
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
