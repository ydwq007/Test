# -*- coding: utf-8 -*-
"""
接口：执行登录用例
创建人：曾卓
更新人：曾卓
更新时间：2020-06-03 16:48
描述：
"""

import unittest,time
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), ".."))+"/Common")
import Run_cases
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), ".."))+"/TestResults")
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), ".."))+"/TestDatas")


class RunCase(unittest.TestCase):# 继承unittest.TestCase

    def test_case(self):

        #参数配置
        self.casespath = "../TestCases/Test_Login" #执行前需检验路径和文件
        self.casesname = "Test_" #执行文件
        # self.style = 3 #发送邮件风格 默认为HTML风格
        self.result_name = "登录相关" # 报告名称

        # 初始化参数
        TEST = Run_cases.Run_Case(self.casespath,self.casesname,self.result_name)
        # 执行用例
        TEST.run_suit(TEST.creat_suit())

if __name__=="__main__":
    unittest.main()#执行所有案例