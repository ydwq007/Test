# -*- coding: utf-8 -*-
"""
接口：执行测试案例-Linux使用
创建人：魏奇
更新人：魏奇
更新时间：2019-07-11
"""
import unittest,time
import sys
sys.path.append("../Common") #跨目录调用需要配置路径
import Run_cases

class RunCase(unittest.TestCase):# 继承unittest.TestCase

    def test_case(self):

        #参数配置
        self.casespath = "../TestCases/Test_Form" #执行前需检验路径和文件
        self.casesname = "Test_Form" #执行文件
        self.result_name = "投票相关" #报告名称

        # 初始化参数
        TEST = Run_cases.Run_Case(self.casespath,self.casesname,self.result_name)
        # 执行用例
        TEST.run_suit(TEST.creat_suit())


if __name__=="__main__":
    unittest.main()#执行所有案例

