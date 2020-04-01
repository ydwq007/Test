# -*- coding: utf-8 -*-
"""
接口：0元订单
创建人：魏奇
更新人：魏奇
更新时间：2020-02-07 16:01
描述：
"""

import unittest,sys,json
sys.path.append("../../Commom")
import Excel,Plan,Excel_Manage,Data_Structure
sys.path.append("../../TestDatas")
import config

Test_Url = config.test_url_mall # mall地址
filepath = config.filepath # 用例文件
resheetname = "zero_order_create" # 用例表名
# loginsheet = "login_moblie" # 用例表名
loginurl = config.test_url_chome # 登录地址
Nomal_login_data = config.aloneA # 纯A账号
shop_login_data = config.dealer # 关联B账号
headers = config.headers # 登录信息头
zero_order = json.dumps(config.zero_order) # 0元订单

class Zero_Order_Create(Plan.Plan):

    def test_zero_order_create_case_00(self):
        """登录更改Authorization"""
        try:
            # 登录
            Auserlogin = Data_Structure.get_token(loginurl,Nomal_login_data,headers) # A账号登录
            Buserlogin = Data_Structure.get_token(loginurl,shop_login_data,headers)# B账号登录

            #更新数据
            mdvalue1 = Buserlogin[2]
            mdvalue2 = Auserlogin[2]
            excel_xl = Excel_Manage.excelprocess_xl()
            # 修改第5行到17行的第5列的值
            excel_xl.write_excel_xls_modify(filepath,17,5,mdvalue1,sheet_name=resheetname,style=3,original_row=5) # 修改第5行到17行的第5列的值(请求头)
            excel_xl.write_excel_xls_modify(filepath,7,6,zero_order,sheet_name=resheetname,style=3,original_row=4) # 修改第4行到5行的第6列的值(请求参数)
            excel_xl.write_excel_xls_modify(filepath,4,5,mdvalue2,sheet_name=resheetname,style=1) # 修改第4行第5列的值(请求头)
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_zero_order_create_case_01(self):
        """正常订单数据（含B类账号）"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"zero_order_create_case_01",Test_Url)
            self.assertEqual(True, result[0])
            # print(result)
            zero_order_id = result[1]["data"]["data"]["order_id"]
            return zero_order_id #返回创建成功的普通订单id
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_zero_order_create_case_02(self):
        """用户未登录"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"zero_order_create_case_02",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_zero_order_create_case_03(self):
        """token失效"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"zero_order_create_case_03",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_zero_order_create_case_04(self):
        """user_id-非必填"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"zero_order_create_case_04",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_zero_order_create_case_05(self):
        """goods_sku_list-必填"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"zero_order_create_case_05",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_zero_order_create_case_06(self):
        """goods_sku_list-商品不存在"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"zero_order_create_case_06",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_zero_order_create_case_07(self):
        """buyer_org_id-必填"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"zero_order_create_case_07",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_zero_order_create_case_08(self):
        """buyer_org_id-客户单位不存在"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"zero_order_create_case_08",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_zero_order_create_case_09(self):
        """buyer_org_id-客户单位不匹配"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"zero_order_create_case_09",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_zero_order_create_case_10(self):
        """service_org_id-必填"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"zero_order_create_case_10",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_zero_order_create_case_11(self):
        """service_org_id-经销商不存在"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"zero_order_create_case_11",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_zero_order_create_case_12(self):
        """service_org_id-经销商不匹配"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"zero_order_create_case_12",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_zero_order_create_case_13(self):
        """company_name-必填"""
        # 这个场景有问题，没有校验必填
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"zero_order_create_case_13",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_zero_order_create_case_14(self):
        """contact_name-非必填"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"zero_order_create_case_14",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_zero_order_create_case_15(self):
        """contact_phone-必填"""
        # 这个场景有问题，没有校验必填
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"zero_order_create_case_15",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_zero_order_create_case_16(self):
        """正常订单数据（纯A类账号）"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"zero_order_create_case_16",Test_Url)
            self.assertEqual(True, result[0])
            # print(result)
            zero_order_id = result[1]["data"]["data"]["order_id"]
            return zero_order_id #返回创建成功的普通订单id
        except Exception as err:
            raise
        finally:
            print("调用接口结束")


if __name__ == "__main__":
    unittest.main()
