# -*- coding: utf-8 -*-
"""
接口：普通订单的流程操作
创建人：魏奇
更新人：魏奇
更新时间：2020-01-17 10:27
描述：
"""

import unittest,sys
sys.path.append("../../Commom")
import Excel,Plan,Excel_Manage,Data_Structure
sys.path.append("../../TestDatas")
import config

Test_Url = config.test_url_mall # mall地址
filepath = config.filepath # 用例文件
resheetname = "normal_order_procedure" # 用例表名
# loginsheet = "login_moblie" # 用例表名
loginurl = config.test_url_chome # 登录地址
Nomal_login_data = config.aloneA # 纯A账号
shop_login_data = config.dealer # 关联B账号
headers = config.headers # 登录信息头
nomal_order = config.nomal_order # 普通订单

class Nomal_Order_Procedure(Plan.Plan):

    def test_nomal_order_create_case_00(self):
        """登录更改Authorization"""
        try:
            # 登录
            Auserlogin = Data_Structure.get_token(loginurl,Nomal_login_data,headers) # A账号登录
            Buserlogin = Data_Structure.get_mallid(loginurl,Test_Url,shop_login_data,headers)# B账号登录

            #更新数据
            mdvalue1 = Auserlogin[4]
            mdvalue3 = Auserlogin[2]
            mdvalue2 = Buserlogin[2]

            # # 商务登录
            # business_login_data = {
            #     "m":"userMobileLogin",
            #     "a":"login",
            #     "username":"15982280117",
            #     "password":"123456",
            #     "account_type":"1"
            # }
            # business_login_request = requests.post(url=login_url,data=json.dumps(business_login_data),headers=config.headers,verify=False)
            # business_login_result= json.loads(business_login_request.text)
            # print(business_login_result)
            # business_login_token = business_login_result["data"]["token"]["access_token"]
            # #更新数据
            # value3 = """{
            #         "Content-Type": "application/json",
            #         "Authorization":"Bearer %s"
            #     }""" % business_login_token
            # mdvalue3 = "%s" % value3
            #
            # print(Nomal_login_request.headers)
            # print(mdvalue1)
            # print(shop_login_request.headers)
            # print(mdvalue2)
            # print(business_login_request.headers)
            # print(mdvalue3)

            # 修改用例中的content-type
            excel_xl = Excel_Manage.excelprocess_xl()
            # 修改普通用户数据
            excel_xl.write_excel_xls_modify(filepath,19,5,mdvalue3,sheet_name=resheetname,style=3,original_row=16) # 修改第26行到19行的第5列的值(请求头)
            excel_xl.write_excel_xls_modify(filepath,23,5,mdvalue1,sheet_name=resheetname,style=3,original_row=20) # 修改第20行到23行的第5列的值(请求头)
            # 修改商家用户数据
            excel_xl.write_excel_xls_modify(filepath,35,5,mdvalue2,sheet_name=resheetname,style=3,original_row=24) # 修改第24行到35行的第5列的值(请求头)
            # # 修改商务数据
            # excel_xl.write_excel_xls_modify(filepath,41,5,mdvalue3,sheet_name=resheetname,style=3,original_row=36)

        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_01(self):
        """普通订单-取消-正常数据"""
        # 场景

        try:
            # 创建订单
            order = Data_Structure.nomal_create(loginurl,Nomal_login_data,headers,Test_Url,nomal_order) # A账号登录并创建普通订单
            mdvalue = order[2]
            # 修改用例中的订单编号
            excel_xl = Excel_Manage.excelprocess_xl()
            excel_xl.write_excel_xls_modify(filepath,16,6,mdvalue,sheet_name=resheetname,style=1)
            excel_xl.write_excel_xls_modify(filepath,20,6,mdvalue,sheet_name=resheetname,style=1)


        # 取消订单
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_01",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_02(self):
        # 这个场景有问题，没有判断订单所属
        """普通订单-取消-非当前账号数据"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_02",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_03(self):
        """普通订单-取消-未登录"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_03",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_04(self):
        """普通订单-取消-状态不正确"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_04",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_05(self):
        # 这个场景有问题，没有判断订单是否存在
        """普通订单-取消-订单号不存在"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_05",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_06(self):
        """普通订单-取消-登录失效"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_06",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_35(self):
        """普通订单-普通用户删除"""

        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_35",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_36(self):
        """普通订单-普通用户删除-未登录"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_36",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_37(self):
        """普通订单-普通用户删除-状态不正确"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_37",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_38(self):
        # 这个场景有问题，没有判断订单是否存在
        """普通订单-普通用户删除-订单不存在"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_38",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_39(self):
        # 这个场景有问题，没有判断登录有效性
        """普通订单-普通用户删除-登录信息失效"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_39",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_40(self):
        # 这个场景有问题，没有判断订单所属
        """普通订单-普通用户删除-非当前用户的订单"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_40",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
             print("调用接口结束")

    def test_nomal_order_procedure_case_07(self):
        # 这个场景有问题，同一个订单可以取消多次
        """普通订单-经销商取消"""

        try:
            # 创建订单
            order = Data_Structure.nomal_create(loginurl,Nomal_login_data,headers,Test_Url,nomal_order) # A账号登录并创建普通订单
            mdvalue = order[2]
            # 修改用例中的订单编号
            excel_xl = Excel_Manage.excelprocess_xl()
            excel_xl.write_excel_xls_modify(filepath,24,6,mdvalue,sheet_name=resheetname,style=1)
            excel_xl.write_excel_xls_modify(filepath,32,6,mdvalue,sheet_name=resheetname,style=1)

            # 取消订单
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_07",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_08(self):
        """普通订单-经销商取消-非当前经销商的订单"""
        # 这个场景有问题，非当前经销商的订单取消成功
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_08",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_09(self):
        """普通订单-经销商取消-未登录"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_09",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_10(self):
        """普通订单-经销商取消-状态不正确"""
        # 这个场景有问题，没有校验订单状态
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_10",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_11(self):
        """普通订单-经销商取消-订单不存在"""
        # 这个场景有问题，没有校验订单是否存在
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_11",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_12(self):
        """普通订单-经销商取消-登录信息失效"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_12",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_13(self):
        """普通订单-经销商确认"""
        try:
            # 创建订单
            order = Data_Structure.nomal_create(loginurl,Nomal_login_data,headers,Test_Url,nomal_order) # A账号登录并创建普通订单
            mdvalue = order[2]
            # 修改用例中的订单编号
            excel_xl = Excel_Manage.excelprocess_xl()
            excel_xl.write_excel_xls_modify(filepath,28,6,mdvalue,sheet_name=resheetname,style=1)

            # 确认订单
            excel_xl.write_excel_xls_modify(filepath,28,6,mdvalue,sheet_name=resheetname,style=1)
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_13",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_14(self):
        """普通订单-经销商确认-非当前经销商的订单"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_14",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_15(self):
        """普通订单-经销商确认-未登录"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_15",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_16(self):
        """普通订单-经销商确认-状态不正确"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_16",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_17(self):
        """普通订单-经销商确认-订单不存在"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_17",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_18(self):
        """普通订单-经销商确认-登录信息失效"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_18",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_29(self):
        """普通订单-经销商订单删除"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_29",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_30(self):
        """普通订单-经销商订单删除-未登录"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_30",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_31(self):
        """普通订单-经销商订单删除-状态不正确"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_31",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_procedure_case_32(self):
        """普通订单-经销商订单删除-订单不存在"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_32",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")


    def test_nomal_order_procedure_case_33(self):
        """普通订单-经销商订单删除-登录信息失效"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_33",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")



    def test_nomal_order_procedure_case_34(self):
        """普通订单-经销商订单删除-非当前经销商的订单"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_34",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")


    # 订单商务部分，由于chome不支持接口直接调用，暂时无法进行接口测试，涉及普通订单，定制单，退货单，换货单
    # def test_nomal_order_procedure_case_19(self):
    #     """普通订单-商务取消"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_19",loginurl)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")

    # def test_nomal_order_procedure_case_20(self):
    #     """普通订单-商务取消-未登录"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_20",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_21(self):
    #     """普通订单-商务取消-状态不正确"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_21",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_22(self):
    #     """普通订单-商务取消-订单不存在"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_22",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_23(self):
    #     """普通订单-商务取消-登录信息失效"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_23",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_24(self):
    #     """普通订单-商务确认"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_24",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")

    # def test_nomal_order_procedure_case_25(self):
    #     """普通订单-商务确认-未登录"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_25",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_26(self):
    #     """普通订单-商务确认-状态不正确"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_26",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    #
    # def test_nomal_order_procedure_case_27(self):
    #     """普通订单-商务确认-订单不存在"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_27",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_28(self):
    #     """普通订单-商务确认-登录信息失效"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_28",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")





if __name__ == "__main__":
    unittest.main()