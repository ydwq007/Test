# -*- coding: utf-8 -*-
"""
接口：
创建人：甯瑛
更新人：甯瑛
更新时间：2020/4/30 16:55
描述：
"""
# -*- coding: utf-8 -*-
"""
接口：
创建人：甯瑛
更新人：甯瑛
更新时间：2020/4/30 16:28
描述：案例搜索
"""
import unittest, sys, json

sys.path.append("../../Commom")
import Excel, Plan, Excel_Manage, Data_Structure

sys.path.append("../../TestDatas")
import config

Test_Url = config.test_url_mall  # mall地址
filepath = config.filepath  # 用例文件
resheetname = "search_cases"  # 用例表名


# loginsheet = "login_moblie" # 用例表名
# loginurl = config.test_url_chome # 登录地址
# Nomal_login_data = config.aloneA # 纯A账号
# shop_login_data = config.dealer # 关联B账号
# headers = config.headers # 登录信息头
# zero_order = json.dumps(config.zero_order) # 0元订单

class SearchProvider(Plan.Plan):
    def test_search_cases_01(self):
        """案例搜索-企业"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_cases_case_01", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_cases_02(self):
        """案例搜索-政务"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_cases_case_02", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_cases_03(self):
        """案例搜索-关键字（kewords）非必填"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_cases_case_03", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_cases_04(self):
        """案例搜索-首页（page_index，page_size）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_cases_case_04", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_cases_05(self):
        """案例搜索_非首页（page_index，page_size）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_cases_case_05", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_cases_06(self):
        """案例搜索-标签id集合（group_id）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_cases_case_06", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_cases_07(self):
        """案例搜索-政企归属（access_identity）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_cases_case_07", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_cases_08(self):
        """案例搜索-上架时间排序降序（update_time_sort:desc）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_cases_case_08", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_cases_09(self):
        """案例搜索-上架时间排序升序（update_time_sort:asc）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_cases_case_09", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_cases_10(self):
        """案例搜索-平均分排序降序（avg_star_sort:desc）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_cases_case_10", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_cases_11(self):
        """案例搜索-平均分排序升序（avg_star_sort:asc）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_cases_case_11", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_cases_12(self):
        """案例搜索-浏览量排序降序（click_sort:desc）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_cases_case_12", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_cases_13(self):
        """案例搜索-浏览量排序升序（click_sort:asc）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_cases_case_13", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_cases_14(self):
        """案例搜索-案例类型（case_type:0默认标准）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_cases_case_14", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")


    def test_search_cases_15(self):
        """案例搜索-案例类型（case_type:1定制案例）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_cases_case_15", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_cases_16(self):
        """案例搜索-案例类型（case_type:2解决方案）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_cases_case_16", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_cases_17(self):
        """案例搜索-案例类型（case_type:3伙伴详情）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_cases_case_17", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")