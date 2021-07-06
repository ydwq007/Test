# -*- coding: utf-8 -*-
"""
接口：
创建人：杜海燕
更新人：杜海燕
更新时间：2021/4/28 16:55
描述：档案编号查询产品信息
"""

import unittest, sys, json, logging

sys.path.append("../../Commom")
import Excel, Plan, Excel_Manage

sys.path.append("../../TestDatas")
import config

Test_Url = config.test_url_dhome  # dhome测试环境地址
filepath = config.filepath_test_dhy  # 用例文件
resheetname = "find_products"  # 用例表名


class SearchProvider(Plan.Plan):

    def test_find_products_01(self):    # 已有正确档案编号查询产品信息
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx(filepath, resheetname, "test_find_products_01", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as errs:
            logging.exception("出现问题")
            raise errs
        finally:
            print("\n调用接口结束")


    # def test_find_products_02(self):    # 统一社会信用代码包含空格
    #     try:
    #         # file = Excel.open_xlsx(filepath)
    #         result = Excel.run_xlsx(filepath, resheetname, "test_find_products_02", Test_Url)
    #         self.assertEqual(True, result[0])
    #
    #     except Exception as err:
    #         raise
    #     finally:
    #         print("\n调用接口结束")



if __name__=="__main__":
    unittest.main()     #执行所有案例

