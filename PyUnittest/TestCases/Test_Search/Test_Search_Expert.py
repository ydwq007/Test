# -*- coding: utf-8 -*-
"""
接口：
创建人：甯瑛
更新人：甯瑛
更新时间：2020/4/30 16:28
描述：专家搜索
"""
import unittest, sys, json

sys.path.append("../../Commom")
import Excel, Plan, Excel_Manage, Data_Structure

sys.path.append("../../TestDatas")
import config

Test_Url = config.test_url_mall  # mall地址
filepath = config.filepath  # 用例文件
resheetname = "search_expert"  # 用例表名


# loginsheet = "login_moblie" # 用例表名
# loginurl = config.test_url_chome # 登录地址
# Nomal_login_data = config.aloneA # 纯A账号
# shop_login_data = config.dealer # 关联B账号
# headers = config.headers # 登录信息头
# zero_order = json.dumps(config.zero_order) # 0元订单

class SearchExpert(Plan.Plan):
    def test_search_expert_01(self):
        """专家搜索-企业"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_expert_case_01", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_expert_02(self):
        """专家搜索-政务"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_expert_case_02", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_expert_03(self):
        """专家搜索-关键字（kewords）非必填"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_expert_case_03", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_expert_04(self):
        """专家搜索-首页（page_index，page_size）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_expert_case_04", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_expert_05(self):
        """专家搜索_非首页（page_index，page_size）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_expert_case_05", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")


    def test_search_expert_06(self):
        """专家搜索-标签id集合（group_id）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_expert_case_06", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_expert_07(self):
        """专家搜索-政企归属（access_identity）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_expert_case_07", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")