# -*- coding: utf-8 -*-
"""
接口：执行测试商品相关测试案例
创建人：魏奇
更新人：魏奇
更新时间：2019-08-20
"""
import unittest,time
import sys
sys.path.append("../Common") #跨目录调用需要配置路径
import Run_cases

class RunCase(unittest.TestCase):# 继承unittest.TestCase

    def test_case(self):

        #参数配置
        self.casespath = "../TestCases/Test_Addcart" #执行前需检验路径和文件
        self.casesname = "Test_Addcart" #执行文件
        self.result_name = "购物车相关" #报告名称

        # 初始化参数
        TEST = Run_cases.Run_Case(self.casespath,self.casesname,self.test_result,self.result_name,self.style)
        # 执行用例
        TEST.run_suit(TEST.creat_suit())


if __name__=="__main__":
    unittest.main()#执行所有案例
