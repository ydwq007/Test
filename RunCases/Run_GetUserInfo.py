#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/6/8 9:04
# @Author : wujj
# @File : Run_GetUserInfo.py


import unittest,time
import sys
sys.path.append("../Common") #跨目录调用需要配置路径
import Run_cases
sys.path.append("../TestResults")


class RunCase(unittest.TestCase):# 继承unittest.TestCase

    def test_case(self):

        #参数配置
        self.casespath = "../TestCases/Test_Wechat" #执行前需检验路径和文件
        self.casesname = "Test_" #执行文件
        self.result_name = "获取微信用户信息" # 报告名称

        # 初始化参数
        TEST = Run_cases.Run_Case(self.casespath,self.casesname,self.result_name)
        # 执行用例
        TEST.run_suit(TEST.creat_suit())

if __name__=="__main__":
    unittest.main()#执行所有案例