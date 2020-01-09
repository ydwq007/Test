# -*- coding: utf-8 -*-
"""
接口：普通订单的创建
创建人：魏奇
更新人：魏奇
更新时间：2020-01-08 9:23
描述：
"""

import unittest,sys
sys.path.append("../../Commom")
import Excel,Plan


class Nomal_Order_Create(Plan.Plan):

    def test_nomal_order_create_case_01(self):
        """正常数据"""
        try:
            file = Excel.open_xlsx("../../TestDatas/接口测试用例.xlsx")
            result = Excel.run_xlsx1(file,"normal_order_create","normal_order_create_case_01","https://testcloud.seeyon.com")
            self.assertEqual(True, result)
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_create_case_02(self):
        """用户未登录"""
        try:
            file = Excel.open_xlsx("../../TestDatas/接口测试用例.xlsx")
            result = Excel.run_xlsx1(file,"normal_order_create","normal_order_create_case_02","https://testcloud.seeyon.com")
            self.assertEqual(True, result)
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_nomal_order_create_case_03(self):
        """用户未登录"""
        try:
            file = Excel.open_xlsx("../../TestDatas/接口测试用例.xlsx")
            result = Excel.run_xlsx1(file,"normal_order_create","normal_order_create_case_03","https://testcloud.seeyon.com")
            self.assertEqual(True, result)
        except Exception as err:
            raise
        finally:
            print("调用接口结束")


if __name__ == "__main__":
    unittest.main()
