# -*- coding: utf-8 -*-
"""
接口：执行测试案例
创建人：魏奇
更新人：魏奇
更新时间：2019-07-11
"""
import unittest
import os,xmlrunner
import time
import HTMLTestRunner_Chart as HTMLTestRunner
import sys
sys.path.append(r"..\Common") #跨目录调用需要配置路径
from SendEmail import sendemail


class RunCase(unittest.TestCase):# 继承unittest.TestCase

    def test_case(self):

        #执行路径
        # casespath = r"..\TestCases" #执行前需检验路径和文件
        casespath = "../TestCases" #执行前需检验路径和文件
        #执行文件
        casesname = "login"
        #执行时间
        run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        #报告名称
        result_name = "%s_接口测试报告_%s" % (casesname,run_time)
        #执行人员
        tester = "魏奇"

        #指定的case所在的路径里寻找所有名称模式匹配pattern的文件并加载其内容
        suite = unittest.TestSuite()#创建测试套件
        os.chdir(casespath) #需要执行的case所在路径
        case_path = os.getcwd() #获取路径
        all_cases = unittest.defaultTestLoader.discover(case_path,pattern="%s*.py" % casesname) #指定案例脚本
        for case in all_cases:
             suite.addTests(case)#把所有的测试用例添加进来

        # #执行并且输出测试报告txt格式
        # with open(r"..\TestResults\test_result.txt", "w", encoding="utf-8") as result_txt: #测试报告路径
        #     runner_tests = unittest.TextTestRunner(stream=result_txt,descriptions=result_txt1,verbosity=2) # verbosity执行结果的详细程度，0<1<2，默认1
        #     runner_tests.run(suite)

        # #执行并且输出测试报告html格式
        # with open(r"..\TestResults\test_result.html", "wb") as result_html: #测试报告路径
        #     runner_results = HTMLTestRunner.HTMLTestRunner(stream=result_html,title=result_name,description="案例具体测试情况，请阅读附件，谢谢",
        #                                                    verbosity=2)
        #     runner_results.run(suite) #执行案例
        with open(r"..\TestResults\test_result.html", "wb") as result_html: #测试报告路径
            runner_results = HTMLTestRunner.HTMLTestRunner(stream=result_html,title=result_name,description="案例具体测试情况，请阅读附件",
                                                    verbosity=2,retry=2,save_last_try=False)
            runner_results.run(suite) #执行案例

        # #执行并且输出测试报告xml格式
        # runner_results = xmlrunner.XMLTestRunner(output=r'..\TestResults')#指定报告放的目录
        # runner_results.run(suite) #执行案例



        #发送测试报告
        time.sleep(5)
        sendemail()

if __name__=="__main__":
    unittest.main()#执行所有案例

