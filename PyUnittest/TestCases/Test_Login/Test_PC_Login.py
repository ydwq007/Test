# -*- coding: utf-8 -*-
"""
接口：
创建人：曾卓
更新人：曾卓
更新时间：2020/6/3 16:51
描述：PC登录
"""

import Excel, Plan, Excel_Manage, Data_Structure
import config

Test_Url = config.test_url_mall  # mall地址
Test_Chome_Url = config.test_url_chome  # mall地址
filepath = config.filepath  # 用例文件
resheetname = "login_pc"  # 用例表名


class PcLogin(Plan.Plan):
    def test_pc_login_01(self):
        """pc登录-无效用户名"""
        try:
            result = Excel.run_xlsx1(filepath, resheetname, "test_pc_login_01", Test_Chome_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")


    def test_pc_login_02(self):
        """pc登录-无效密码"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "test_pc_login_02", Test_Chome_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

    def test_pc_login_03(self):
        """pc登录-无效密码"""
        try:
            # file = Excel.open_xlsx(filepath)
            result = Excel.run_xlsx1(filepath, resheetname, "test_pc_login_03", Test_Chome_Url)
            self.assertEqual(True, result[0])
        except Exception as err:
            raise
        finally:
            print("调用接口结束")

