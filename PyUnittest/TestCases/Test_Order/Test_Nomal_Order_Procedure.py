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
import Excel,Plan
sys.path.append("../../TestDatas")
import config

Test_Url = config.test_url_mall
filepath = config.filepath
resheetname = "normal_order_procedure"

class Nomal_Order_Procedure(Plan.Plan):
    #
    # def test_nomal_order_procedure_case_01(self):
    #     """普通订单-取消-正常数据"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_01",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_02(self):
    #     # 这个场景有问题
    #     """普通订单-取消-非当前账号数据"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_02",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_03(self):
    #     """普通订单-取消-未登录"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_03",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_04(self):
    #     """普通订单-取消-状态不正确"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_04",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_05(self):
    #     # 这个场景有问题
    #     """普通订单-取消-订单号不存在"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_05",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_06(self):
    #     """普通订单-取消-登录失效"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_06",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")

    # def test_nomal_order_procedure_case_07(self):
    #     """普通订单-经销商取消"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_07",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")

    # def test_nomal_order_procedure_case_08(self):
    #     """普通订单-经销商取消-非当前经销商的订单"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_08",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_09(self):
    #     """普通订单-经销商取消-未登录"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_09",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_10(self):
    #     """普通订单-经销商取消-状态不正确"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_10",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_11(self):
    #     """普通订单-经销商取消-订单不存在"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_11",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")

    # def test_nomal_order_procedure_case_12(self):
    #     """普通订单-经销商取消-登录信息失效"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_12",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_13(self):
    #     """普通订单-经销商确认"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_13",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_14(self):
    #     """普通订单-经销商确认-非当前经销商的订单"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_14",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_15(self):
    #     """普通订单-经销商确认-未登录"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_15",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_16(self):
    #     """普通订单-经销商确认-状态不正确"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_16",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_17(self):
    #     """普通订单-经销商确认-订单不存在"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_17",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_18(self):
    #     """普通订单-经销商确认-登录信息失效"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_18",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_19(self):
    #     """普通订单-商务取消"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_19",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
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
    #
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
    #
    # def test_nomal_order_procedure_case_29(self):
    #     """普通订单-经销商订单删除"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_29",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_30(self):
    #     """普通订单-经销商订单删除-未登录"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_30",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_31(self):
    #     """普通订单-经销商订单删除-状态不正确"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_31",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_32(self):
    #     """普通订单-经销商订单删除-订单不存在"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_32",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    #
    # def test_nomal_order_procedure_case_33(self):
    #     """普通订单-经销商订单删除-登录信息失效"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_33",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    #
    #
    # def test_nomal_order_procedure_case_34(self):
    #     """普通订单-经销商订单删除-非当前经销商的订单"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_34",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
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

    # def test_nomal_order_procedure_case_36(self):
    #     """普通订单-普通用户删除-未登录"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_36",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")

    # def test_nomal_order_procedure_case_37(self):
    #     """普通订单-普通用户删除-状态不正确"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_37",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_38(self):
    #     """普通订单-普通用户删除-订单不存在"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_38",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_39(self):
    #     """普通订单-普通用户删除-登录信息失效"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_39",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_nomal_order_procedure_case_40(self):
    #     """普通订单-普通用户删除-非当前用户的订单"""
    #     try:
    #         file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_40",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")



if __name__ == "__main__":
    unittest.main()