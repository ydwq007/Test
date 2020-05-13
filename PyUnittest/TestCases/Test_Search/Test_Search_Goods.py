# -*- coding: utf-8 -*-
"""
接口：
创建人：甯瑛
更新人：甯瑛
更新时间：2020/4/28 10:13
描述：商品搜索
"""
import unittest, sys, json

sys.path.append("../../Commom")
import Excel, Plan, Excel_Manage, Data_Structure

sys.path.append("../../TestDatas")
import config

Test_Url = config.test_url_mall  # mall地址
filepath = config.filepath  # 用例文件
resheetname = "search_goods"  # 用例表名


# loginsheet = "login_moblie" # 用例表名
# loginurl = config.test_url_chome # 登录地址
# Nomal_login_data = config.aloneA # 纯A账号
# shop_login_data = config.dealer # 关联B账号
# headers = config.headers # 登录信息头
# zero_order = json.dumps(config.zero_order) # 0元订单

class SearchGoods(Plan.Plan):

    def test_search_goods_01(self):
        """商品搜索-企业搜索"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_01", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_02(self):
        """商品搜索-政务搜索"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_02", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")
    def test_search_goods_03(self):
        """商品搜索-关键字（kewords）非必填"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_03", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")


    def test_search_goods_04(self):
        """商品搜索-全部商品"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_04", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_05(self):
        """商品搜索-应用产品"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_05", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_06(self):
        """商品搜索-解决方案"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_06", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_07(self):
        """商品搜索-表单模板"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_07", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_08(self):
        """商品搜索-工具组件"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_08", Test_Url)
            self.assertEqual(True, result[0])

        except Exception as err:
            raise
        finally:
            print("调用接口结束")


    def test_search_goods_09(self):
        """商品搜索-服务产品"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_09", Test_Url)
            print(result)
            #self.assertEqual(True, result[0])


        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_10(self):
        """商品搜索-首页（page_index，page_size）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_10", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_11(self):
        """商品搜索_非首页（page_index，page_size）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_11", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_12(self):
        """商品搜索_销量排序降序（sale:desc)"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_12", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_13(self):
        """商品搜索_销量排序升序（sale:asc)"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_13", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_14(self):
        """商品搜索_上架时间排序降序（up_time_sort:desc）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_14", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_15(self):
        """商品搜索_上架时间排序升序（up_time_sort:asc）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_15", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_16(self):
        """商品搜索_价格排序降序（price_sort:desc）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_16", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_17(self):
        """商品搜索_价格排序升序（price_sort:asc）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_17", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_18(self):
        """商品搜索_下载量排序降序（download_sort:desc）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_18", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_19(self):
        """商品搜索_下载量排序升序（download_sort:asc）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_19", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_20(self):
        """商品搜索_平均分排序降序（avg_star_sort:desc）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_20", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_21(self):
        """商品搜索_平均分排序升序（avg_star_sort:asc）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_21", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_22(self):
        """商品搜索_浏览量排序升序（click_sort:desc）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_22", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_23(self):
        """商品搜索_浏览量排序降序（click_sort:asc）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_23", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_24(self):
        """商品搜索_分类id（category_id）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_24", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_25(self):
        """商品搜索_标签id集合（group_ids）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_25", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_26(self):
        """商品搜索_体验中心列表（experience_center）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_26", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_27(self):
        """商品搜索_商品id（goods_id）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_27", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_28(self):
        """商品搜索_价格类型（price_type）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_28", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_29(self):
        """商品搜索_V5产品版本（product_version）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_29", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_30(self):
        """商品搜索_政企归属（access_identity）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_30", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_search_goods_31(self):
        """商品搜索_集合类型（collection_types）"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "search_goods_case_31", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")