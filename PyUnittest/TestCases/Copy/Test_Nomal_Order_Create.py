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
sys.path.append("../../TestDatas")
import config


Test_Url = config.test_url_mall
filepath = "../../TestDatas/接口测试用例.xlsx"
resheetname = "normal_order_create"

class Nomal_Order_Create(Plan.Plan):

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
