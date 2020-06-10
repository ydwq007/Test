# -*- coding: utf-8 -*-
"""
接口：创建定制单
创建人：魏奇
更新人：魏奇
更新时间：2020-02-25 11:10
描述：
"""

import unittest,sys,json
# sys.path.append("../../Commom")
import Excel,Plan,Excel_Manage,Data_Structure
# sys.path.append("../../TestDatas")
import config

Test_Url = config.test_url_mall # mall地址
Test_file = config.test_url_file
filepath = config.filepath # 用例文件
resheetname = "custom_order" # 用例表名

class Custom_Order(Plan.Plan):

    def test_custom_order_case_01(self):
        """定制单创建-未登录"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_01", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_02(self):
        """定制单创建-token失效"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_02", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_03(self):
        """定制单创建-正常定制单(参考商品)"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_03", Test_Url)
            self.assertEqual(True, result[0])
            re = tuple(result[1].values()) #获取元组中的值
            orderId = re[1]["orderId"]
            mdvalue1 = json.dumps({"user_id": "15730961430270000","order_id": orderId})
            mdvalue2 = json.dumps({"order_id": orderId})
            excel_xl = Excel_Manage.excelprocess_xl()
            excel_xl.write_excel_xls_modify(filepath,36,9,mdvalue1,sheet_name=resheetname,style=1) # 修改第36行的第9列的值
            excel_xl.write_excel_xls_modify(filepath,44,9,mdvalue2,sheet_name=resheetname,style=1) # 修改第44行的第9列的值
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_04(self):
        """定制单创建-正常定制单(参考案例)"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_04", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_05(self):
        """定制单创建-参考应用为空"""
        # 这个场景有问题
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_05", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_06(self):
        """定制单创建-定制类型为空"""
        # 这个场景有问题
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_06", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_07(self):
        """定制单创建-定制类型错误"""
        # 这个场景有问题
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_07", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_08(self):
        """定制单创建-定制名称为空"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_08", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_09(self):
        """定制单创建-定制需求为空"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_09", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_10(self):
        """定制单创建-需求文档为空"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_10", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    # def test_custom_order_case_11(self):
    #     """定制单创建-单位为空"""
    #     try:
    #         result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_11", Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")

    def test_custom_order_case_12(self):
        """定制单修改-未登录"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_12", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_13(self):
        """定制单修改-token失效"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_13", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_14(self):
        """定制单修改-正常定制单(参考商品)"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_14", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_15(self):
        """定制单修改-正常定制单(参考案例)"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_15", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_16(self):
        """定制单修改-参考应用为空"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_16", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_17(self):
        """定制单修改-定制类型为空"""
         # 这个场景有问题
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_17", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_18(self):
        """定制单修改-定制类型错误"""
        # 这个场景有问题
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_18", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_19(self):
        """定制单修改-定制名称为空"""
        # 这个场景有问题
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_19", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_20(self):
        """定制单修改-定制需求为空"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_20", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_21(self):
        """定制单修改-需求文档为空"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_21", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    # def test_custom_order_case_22(self):
    #     """定制单修改-单位为空"""
    #     # 这个场景有问题
    #     try:
    #         result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_22", Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")

    def test_custom_order_case_23(self):
        """定制单列表"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_23", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_24(self):
        """定制单列表-匹配到结果"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_24", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_25(self):
        """定制单列表-匹配不到结果"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_25", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_26(self):
        """定制单详情-用户id为空"""
        # 这个场景有问题
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_26", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_27(self):
        """定制单详情-用户id不匹配"""
        # 这个场景有问题
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_27", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_28(self):
        """定制单详情-订单id为空"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_28", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_29(self):
        """定制单详情-订单id不匹配"""
         # 这个场景有问题
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_29", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_30(self):
        """定制单详情-用户id和订单id匹配"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_30", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_31(self):
        """定制单取消-用户id为空"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_31", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_32(self):
        """定制单取消-用户id不匹配"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_32", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_33(self):
        """定制单取消-订单id为空"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_33", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_34(self):
        """定制单取消-订单id不匹配"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_34", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_35(self):
        """定制单取消-用户id和订单id匹配可取消"""
        # 这个场景需要实时生成定单id
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_35", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_36(self):
        """定制单取消-用户id和订单id匹配不可取消"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_36", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    # def test_custom_order_case_37(self):
    #     """定制单文件上传-token为空"""
    #     # 这个场景有问题
    #     try:
    #         result = Excel.run_xlsx1(filepath,resheetname,"custom_order_case_37",Test_file)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_custom_order_case_38(self):
    #     """定制单文件上传-token失效"""
    #     # 这个场景有问题
    #     try:
    #         result = Excel.run_xlsx1(filepath,resheetname,"custom_order_case_38",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_custom_order_case_39(self):
    #     """定制单文件上传-文件为空"""
    #     # 这个场景有问题
    #     try:
    #         result = Excel.run_xlsx1(filepath,resheetname,"custom_order_case_39",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")
    #
    # def test_custom_order_case_40(self):
    #     """定制单文件上传-正常上传"""
    #     # 这个场景有问题
    #     try:
    #         result = Excel.run_xlsx1(filepath,resheetname,"custom_order_case_40",Test_Url)
    #         self.assertEqual(True, result[0])
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("调用接口结束")

    def test_custom_order_case_41(self):
        """定制单删除-订单id为空"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_41", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_42(self):
        """定制单删除-订单id不匹配"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_42", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_43(self):
        """定制单删除-订单id匹配可删除"""
        # 需要生成实时定单，并且状态的是取消
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_43", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_44(self):
        """定制单删除-订单id匹配不可删除"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_44", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_45(self):
        """定制单下载-文件存在"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_45", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_46(self):
        """定制单-上传文件token-用户存在"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_46", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_47(self):
        """定制单-上传文件token-用户不存在"""
        # 这个场景有问题
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_47", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_48(self):
        """定制单-上传文件token-用户id为空"""
        # 这个场景有问题
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_48", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_custom_order_case_49(self):
        """定制单下载-文件不存在"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "custom_order_case_49", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

if __name__ == "__main__":
    unittest.main()

