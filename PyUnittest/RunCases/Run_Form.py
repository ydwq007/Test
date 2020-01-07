# -*- coding: utf-8 -*-
"""
接口：执行测试案例-Linux使用
创建人：魏奇
更新人：魏奇
更新时间：2019-07-11
"""
import unittest,os,xmlrunner,time
import sys
sys.path.append("../../Common") #跨目录调用需要配置路径
from SendEmail import sendemail
import HTMLTestRunner_Chart as HTMLTestRunner


class RunCase(unittest.TestCase):# 继承unittest.TestCase

    def test_case(self):
        #参数配置
        self.casespath = "../TestCases/Test_Form" #执行前需检验路径和文件
        self.casesname = "Test_Form" #执行文件
        self.style = 3 #发送邮件风格
        self.run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.run_time1 = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        self.result_name = "%s_接口测试报告_%s" % (self.casesname,self.run_time) #报告名称
        self.tester = "魏奇" #执行人员
        # self.test_reult = "../TestResult/TestResult_%s.html" % self.run_time1
        self.test_reult = r"D:\IdeaProjects\interfacetest\TestResults\TestResult_%s.html" % self.run_time1
        print(self.test_reult)

        #指定的case所在的路径里寻找所有名称模式匹配pattern的文件并加载其内容
        suite = unittest.TestSuite()#创建测试套件
        os.chdir(self.casespath) #需要执行的case所在路径
        self.case_path = os.getcwd() #获取路径
        all_cases = unittest.defaultTestLoader.discover(self.case_path,pattern="%s*.py" % self.casesname) #指定案例脚本
        for case in all_cases:
            suite.addTests(case)#把所有的测试用例添加进来

        ##执行并且输出测试报告
        #txt格式
        if self.style == 1:
            with open("../TestResults/TestResult.txt", "w", encoding="utf-8") as result_txt: #测试报告路径
                runner_results = unittest.TextTestRunner(stream=result_txt,descriptions=result_txt,verbosity=2) # verbosity执行结果的详细程度，0<1<2，默认1
                runner_results.run(suite) #执行案例
        #xml格式
        elif self.style == 2:
            runner_results = xmlrunner.XMLTestRunner(output='../TestResults')#指定报告放的目录
            runner_results.run(suite) #执行案例
        #html格式
        else:
            with open(self.test_reult, "wb") as result_html: #测试报告路径
                runner_results = HTMLTestRunner.HTMLTestRunner(stream=result_html,title=self.result_name,description="案例具体测试情况，请阅读附件",
                                                               verbosity=2) #retry=2,save_last_try=False
                runner_results.run(suite) #执行案例
        #发送测试报告
        time.sleep(3)
        sendemail()

if __name__=="__main__":
    unittest.main()#执行所有案例

