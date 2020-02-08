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
filepath = "../../TestDatas/接口测试用例.xlsx"
resheetname = "normal_order_procedure"

class Nomal_Order_Procedure(Plan.Plan):

    def test_nomal_order_procedure_case_01(self):
        """普通订单-取消-正常数据"""
        try:
            file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(file,resheetname,"normal_order_procedure_case_01",Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    # def test_nomal_order_procedure_case_02(self):
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

if __name__ == "__main__":
    unittest.main()