# -*- coding: utf-8 -*-
"""
接口：
创建人：甯瑛
更新人：甯瑛
更新时间：2020/5/6 11:25
描述：
"""
import unittest, time
import sys

sys.path.append("../Common")  # 跨目录调用需要配置路径
import Run_cases

sys.path.append("../TestResults")


class RunCase(unittest.TestCase):  # 继承unittest.TestCase

    def test_case(self):
        # 参数配置
        self.casespath = "../TestCases/Test_Search"  # 执行前需检验路径和文件
        self.casesname = "Test_"  # 执行文件
        # self.style = 3 #发送邮件风格 默认为HTML风格
        self.result_name = "搜索相关"  # 报告名称

        # 初始化参数
        TEST = Run_cases.Run_Case(self.casespath, self.casesname, self.result_name)
        # 执行用例
        TEST.run_suit(TEST.creat_suit())


if __name__ == "__main__":
    unittest.main()  # 执行所有案例
