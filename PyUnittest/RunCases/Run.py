# -*- coding: utf-8 -*-
"""
接口：执行所有案例
创建人：魏奇
更新人：魏奇
更新时间：2020-02-02 16:56
描述：将不同不同目录下的用例复制到同一目录下，执行案例
"""

import unittest,time,sys,os
# sys.path.append("../Common") #跨目录调用需要配置路径
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), ".."))+"/Common")
import Run_cases,File_Copy
# sys.path.append("../TestResults")
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), ".."))+"/TestResults")
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), ".."))+"/TestDatas")

class RunCase(unittest.TestCase):# 继承unittest.TestCase

    def test_case(self):
        #参数配置
        self.casespath = "../RunCases/Copy/" #执行前需检验路径和文件
        self.casesname = "Test_" #执行文件
        self.result_name = "全用例执行" #报告名称

        # 初始化参数
        TEST = Run_cases.Run_Case(self.casespath,self.casesname,self.result_name)
        # 执行用例
        testcases = TEST.creat_suit()
        TEST.run_suit(testcases)


if __name__=="__main__":
    oldpath = "../TestCases"
    newpath = "../RunCases/Copy/"
    File_Copy.Filedel(newpath)
    File_Copy.CreateFolder(newpath)
    File_Copy.FileCopy(oldpath,newpath)
    unittest.main()#执行所有案例