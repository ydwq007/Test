# -*- coding: utf-8 -*-
"""
接口：执行所有案例
创建人：魏奇
更新人：魏奇
更新时间：2020-02-02 16:56
描述：将不同不同目录下的用例复制到同一目录下，执行案例
"""

import unittest,time,sys
sys.path.append("../Common") #跨目录调用需要配置路径
import Run_cases,File_Copy
sys.path.append("../TestResults")


class RunCase(unittest.TestCase):# 继承unittest.TestCase

    def test_case(self):
        #参数配置
        self.casespath = "../TestCases/Copy/" #执行前需检验路径和文件
        self.casesname = "Test_" #执行文件
        self.style = 3 #发送邮件风格
        self.run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.run_time1 = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        self.result_name = "%s_接口测试报告_%s" % ("全用例执行",self.run_time) #报告名称
        self.tester = "魏奇" #执行人员
        self.test_result = "../../TestResults/TestResult_%s.html" % self.run_time1
        # self.test_reult = "/var/lib/jenkins/workspace/ZY/PyUnittest/TestResults/TestResult_%s.html" % self.run_time1"  # Linux下调试路径指定文件目录

        # 初始化参数
        TEST = Run_cases.Run_Case(self.casespath,self.casesname,self.test_result,self.result_name)
        # 执行用例
        TEST.run_suit(TEST.creat_suit())


if __name__=="__main__":
    oldpath = "../TestCases"
    newpath = "../TestCases/Copy/"
    File_Copy.Filedel(newpath)
    File_Copy.CreateFolder(newpath)
    File_Copy.FileCopy(oldpath,newpath)
    unittest.main()#执行所有案例