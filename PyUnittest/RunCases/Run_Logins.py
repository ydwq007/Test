# -*- coding: utf-8 -*-
"""
接口：执行测试案例-windows使用
创建人：魏奇
更新人：魏奇
更新时间：2019-07-11
"""
import unittest,time
import sys
sys.path.append("../Common") #跨目录调用需要配置路径
import Run_cases
sys.path.append("../../TestResults")


class RunCase(unittest.TestCase):# 继承unittest.TestCase

    def test_case(self):

        #参数配置
        self.casespath = "../TestCases/Test_Login" #执行前需检验路径和文件
        self.casesname = "Test_Login" #执行文件
        self.style = 3 #发送邮件风格
        self.run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.run_time1 = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        self.result_name = "%s_接口测试报告_%s" % ("登录相关",self.run_time) #报告名称
        self.tester = "魏奇" #执行人员
        self.test_result = r"../../TestResults/TestResult_%s.html" % self.run_time1
        # self.test_reult = "/var/lib/jenkins/workspace/ZY/PyUnittest/TestResults/TestResult_%s.html" % self.run_time1"  # Linux下调试路径指定文件目录

        # 初始化参数
        TEST = Run_cases.Run_Case(self.casespath,self.casesname,self.test_result,self.result_name,self.style)
        # 执行用例
        TEST.run_suit(TEST.creat_suit())

if __name__=="__main__":
    unittest.main()#执行所有案例

