# -*- coding: utf-8 -*-
"""
接口：换货单
创建人：魏奇
更新人：魏奇
更新时间：2020-05-08 16:29
描述：
"""

import unittest,sys,json
sys.path.append("../../Commom")
import Excel,Plan,Excel_Manage,Data_Structure
sys.path.append("../../TestDatas")
import config

Test_Url = config.test_url_mall # mall地址
Test_Home = config.test_url_chome
filepath = config.filepath # 用例文件
resheetname = "exchange_order" # 用例表名

class Return_Order(Plan.Plan):

    def test_exchange_order_case_01(self):

        """换货单创建-正常换货单-comment非空，returnReason为选错版本"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_01", Test_Url)
            self.assertEqual(True, result[0])
            re = tuple(result[1].values()) #获取元组中的值
            returnCode = re[2]["returnOrderInfo"]["returnCode"] # 获取换货单号
            mdvalue = json.dumps({"returnCode": returnCode, "returnStatus": -3})
            excel_xl = Excel_Manage.excelprocess_xl()
            excel_xl.write_excel_xls_modify(filepath,34,9,mdvalue,sheet_name=resheetname,style=1) # 修改第34行的第9列的值
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_02(self):

        """换货单创建-正常换货单-comment为空，returnReason为选错商品"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_02", Test_Url)
            self.assertEqual(True, result[0])
            re = tuple(result[1].values())
            returnCode = re[2]["returnOrderInfo"]["returnCode"]
            mdvalue = json.dumps({"returnCode": returnCode, "returnStatus": -1})
            excel_xl = Excel_Manage.excelprocess_xl()
            excel_xl.write_excel_xls_modify(filepath,38,9,mdvalue,sheet_name=resheetname,style=1) # 修改第38行的第9列的值
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")


    def test_exchange_order_case_03(self):

        """换货单创建-orderGoodsId为空"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_03", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_04(self):

        """换货单创建-orderGoodsId不存在"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_04", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_05(self):

        """换货单创建-returnType为空"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_05", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_06(self):

        """换货单创建-returnType值不为2"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_06", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_07(self):

        """换货单创建-returnReason为空"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_07", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_08(self):

        """换货单创建-新产生的orderGoodsId重复"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_08", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_09(self):

        """换货单创建-更换商品为空"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_09", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_10(self):

        """换货单创建-0元商品"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_10", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_11(self):

        """换货单创建-非交易完成状态"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_11", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_12(self):

        """换货单创建-已退货成功"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_12", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_13(self):

        """换货单创建-退货中"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_13", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    # def test_exchange_order_case_14(self):
    #
    #     """换货单创建-单位不匹配"""
    #     try:
    #         # file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_14", Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("\n调用接口结束")

    def test_exchange_order_case_15(self):

        """换货单列表-查询条件为空"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_15", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_16(self):

        """换货单列表-组合查询"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_16", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_17(self):

        """换货单列表-退货类型"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_17", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_18(self):

        """换货单列表-换货单号"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_18", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_19(self):

        """换货单列表-换货单状态"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_19", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_20(self):

        """换货单列表-页数"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_20", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_21(self):

        """换货单列表-每页数量"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_21", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_22(self):

        """换货单列表-时间"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_22", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_23(self):

        """换货单详情-returnCode为空"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_23", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_24(self):

        """换货单详情-returnCode不存在"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_24", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_25(self):

        """换货单详情-returnCode存在"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_25", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_26(self):

        """获取需要退货的订单详情-orderGoodsId存在"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_26", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_27(self):

        """获取需要退货的订单详情-orderGoodsId为空"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_27", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_28(self):

        """获取需要退货的订单详情-orderGoodsId不存在"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_28", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_29(self):

        """取消换货单-returnCode为空"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_29", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_30(self):

        """取消换货单-returnCode不存在"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_30", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_31(self):

        """取消换货单-returnStatus非-3"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_31", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_32(self):

        """取消换货单订单状态非待专属服务机构确认"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_32", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_33(self):

        """取消换货单-正常数据"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_33", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_34(self):

        """换货单审核-returnCode为空"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_34", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_35(self):

        """换货单审核-returnCode不存在"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_35", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_36(self):

        """换货单审核-returnStatus非指定值"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_36", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    def test_exchange_order_case_37(self):

        """换货单审核-经销商拒绝"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_37", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    # def test_exchange_order_case_38(self):
    #
    #     """换货单审核-待商务确认"""
    #     try:
    #         # file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_38", Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("\n调用接口结束")


    # def test_exchange_order_case_42(self):
    #
    #     """换货单创建-正常换货单-comment非空，returnReason为选错商品"""
    #     # 待商务确认和退货成功造数据
    #     try:
    #         # file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_42", Test_Url)
    #         self.assertEqual(True, result[0])
    #         re = tuple(result[1].values())
    #         returnCode = re[2]["returnOrderInfo"]["returnCode"]
    #         mdvalue1 = json.dumps({"returnCode": returnCode, "returnStatus": 2})
    #         mdvalue2 = json.dumps({"returnCode": returnCode, "returnStatus": 3})
    #         excel_xl = Excel_Manage.excelprocess_xl()
    #         excel_xl.write_excel_xls_modify(filepath,39,9,mdvalue1,sheet_name=resheetname,style=1) # 修改第39行的第9列的值
    #         excel_xl.write_excel_xls_modify(filepath,41,9,mdvalue1,sheet_name=resheetname,style=1) # 修改第41行的第9列的值
    #     except Exception as err:
    #             raise
    #     finally:
    #             print("\n调用接口结束")

    # def test_exchange_order_case_43(self):
    #
    #     """换货单创建-正常换货单-comment为空，returnReason为选错商品"""
    #     # 商务拒绝造数据
    #     try:
    #         # file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_43", Test_Url)
    #         self.assertEqual(True, result[0])
    #         re = tuple(result[1].values())
    #         returnCode = re[2]["returnOrderInfo"]["returnCode"]
    #         orderGoodsId = re[2]["returnOrderInfo"]["orderGoodsId"]
    #         mdvalue = json.dumps({"returnCode": returnCode, "returnStatus": -2})
    #         excel_xl = Excel_Manage.excelprocess_xl()
    #         excel_xl.write_excel_xls_modify(filepath,40,9,mdvalue,sheet_name=resheetname,style=1) # 修改第40行的第9列的值
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("\n调用接口结束")
    #
    # def test_exchange_order_case_39(self):
    #
    #     """换货单审核-商务拒绝"""
    #     try:
    #         # file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_39", Test_Home)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("\n调用接口结束")
    #
    # def test_exchange_order_case_40(self):
    #
    #     """换货单审核-退货成功"""
    #     try:
    #         # file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_40", Test_Home)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("\n调用接口结束")

    def test_exchange_order_case_41(self):

        """换货单审核-经销商确认-无权限"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_41", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("\n调用接口结束")

    # def test_exchange_order_case_42(self):
    #
    #     """换货单审核-经销商取消-无权限"""
    #     try:
    #         # file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_42", Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("\n调用接口结束")

    # def test_exchange_order_case_43(self):
    #
    #     """换货单审核-用户取消-无权限"""
    #     try:
    #         # file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_43", Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("\n调用接口结束")

    # def test_exchange_order_case_44(self):
    #
    #     """换货单审核-用户创建-无权限"""
    #     try:
    #         # file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(filepath, resheetname, "exchange_order_case_44", Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("\n调用接口结束")


if __name__ == "__main__":
    unittest.main()