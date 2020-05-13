# -*- coding: utf-8 -*-
"""
接口：执行用例
创建人：魏奇
更新人：魏奇
更新时间：2020-01-07 11:26
描述：
"""

import unittest,os,xmlrunner,time,sys
sys.path.append("../Common") #跨目录调用需要配置路径
import HTMLTestRunner
from SendEmail import sendemail

class Run_Case(object):

    path = "../TestResults"
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print("%s目录创建成功" % path)
    else:
        print("%s 目录已存在" % path)

    # 初始化参数
    def __init__(self,path,casename,result_name,style=3):
        self.run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.result_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        self.path = path
        self.casename = casename
        self.test_result = "../../TestResults/TestResult_%s.html" % self.result_time
        self.result_name = "%s_接口测试报告_%s" % (result_name,self.run_time) #报告名称
        self.style = style

    # 创建测试套件
    def creat_suit(self):

        #指定的case所在的路径里寻找所有名称模式匹配pattern的文件并加载其内容
        suite = unittest.TestSuite()#创建测试套件
        os.chdir(self.path) #需要执行的case所在路径
        case_path = os.getcwd() #获取路径
        all_cases = unittest.defaultTestLoader.discover(case_path,pattern="%s*.py" % self.casename) #指定案例脚本

        for test_case in all_cases:
            # for case in test_case:
            suite.addTests(test_case)#把所有的测试用例添加进来

        return suite


    # 执行并且输出测试报告
    def run_suit(self,suite):

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
            with open(self.test_result, "wb") as result_html: #测试报告路径
                runner_results = HTMLTestRunner.HTMLTestRunner(stream=result_html,title=self.result_name,description="用例具体测试情况，请阅读附件",
                                                               verbosity=2) #retry=2,save_last_try=False
                runner_results.run(suite) #执行案例

        #发送测试报告
        time.sleep(3)
        sendemail(send_content=2,issend=1) #issend是否发送邮件（1是，0否），send_content发送附件（1,字符串，2附件）

