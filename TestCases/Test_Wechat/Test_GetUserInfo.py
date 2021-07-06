#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/5/25 13:39
# @Author : wujj
# @File : Test_GetUserInfo.py



import Excel, Plan, unittest, json, logging
import config, Basic_Interface, Excel_Manage


Test_Url = config.test_url_mall  # 测试环境地址
filepath = config.filepath_test_wjj  # 用例文件
resheetname = "getuserinfo"  # 用例表名

class getuserinfo(Plan.Plan):

    #获取用户信息成功
    def test_get_user_info_01(self):

        try:
            result = Excel.run_xlsx(filepath, resheetname, "test-getuser-01", Test_Url)
            self.assertEqual(True, result[0])
        except Exception as errs:
            logging.exception("出现问题")
            raise errs
        finally:
            print("\n调用接口结束")


if __name__ == "__main__":
    unittest.main()