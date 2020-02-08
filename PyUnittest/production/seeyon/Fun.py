# -*- coding: utf-8 -*-
"""
接口：
创建人：魏奇
更新人：魏奇
更新时间：2019-11-20 17:33
描述：
"""
import pymysql as mysql
import Execute_Log as log
import Request_Interface as request
import Excel_Read as excel
import Constants as cs
from prettytable import PrettyTable
import Json_data

logging = log.get_logger()


class ApiTest:
    """接口测试业务类"""
    filename = cs.FILE_NAME

    def __init__(self):
        pass

    def prepare_data(self, host, user, password, db, sql):
        """数据准备，添加测试数据"""
        mysql.connect(host, user, password, db)
        res = mysql.execute(sql)
        mysql.close()
        logging.info("Run sql: the row number affected is %s", res)
        return res

    def get_excel_sheet(self, path, module):
        """依据模块名获取sheet"""
        excel.open_excel(path)
        return excel.get_sheet(module)

    def get_prepare_sql(self, sheet):
        """获取预执行SQL"""
        return excel.get_content(sheet, cs.SQL_ROW, cs.SQL_COL)

    def run_test(self, sheet, url):
        """再执行测试用例"""
        rows = excel.get_rows(sheet)
        fail = 0
        for i in range(1, rows):
            testNumber = str(int(excel.get_content(sheet, i, cs.CASE_NUMBER)))
            testData = excel.get_content(sheet, i, cs.CASE_DATA)
            # testData = json.dumps(excel.get_content(sheet, i, cs.CASE_DATA) ) #json.dumps()用于将字典形式的数据转化为json字符串
            testName = excel.get_content(sheet, i, cs.CASE_NAME)
            testUrl = excel.get_content(sheet, i, cs.CASE_URL)
            testUrl = url + testUrl
            testMethod = excel.get_content(sheet, i, cs.CASE_METHOD)
            testHeaders = eval(excel.get_content(sheet, i, cs.CASE_HEADERS))
            testCode = excel.get_content(sheet, i, cs.CASE_CODE)
            testExcept = excel.get_content(sheet, i, cs.CASE_EXCEPT)
            actualCode = request.api(testMethod, testUrl, testData, testHeaders)
            expectCode = int(testCode)
            failResults = PrettyTable(["Number", "Method", "Url", "Data", "ActualCode", "ExpectCode"])
            failResults.align = "l" #左对齐
            failResults.padding_width = 1 # 设定左侧填充空白字符
            failResults.sortby = "Number"  # 设定排序方式
            failResults.add_row([testNumber, testMethod, testUrl, testData, actualCode, expectCode])
            print(failResults)
            # allResults = PrettyTable(["Number", "Method", "Url", "Data", "ActualCode", "ExpectCode"])
            # allResults.align["Number"] = "0"
            # allResults.padding_width = 1
            # allResults.add_row([testNumber, testMethod, testUrl, testData, actualCode, expectCode])
            # print(allResults)


            if actualCode != expectCode:
                logging.info("FailCase %s", testName)
                # print("FailureInfo")
                # print(failResults)
                fail += 1
            else:
                logging.info("Number %s", testNumber)
                logging.info("TrueCase %s", testName)

        print(failResults)
        if fail > 0:
            # print(failResults)
            return False
        return True









