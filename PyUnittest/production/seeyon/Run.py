# -*- coding: utf-8 -*-
"""
接口：
创建人：魏奇
更新人：魏奇
更新时间：2019-11-20 17:38
描述：
"""
import Execute_Log as log
from Fun import ApiTest

func = ApiTest()
logging = log.get_logger()

"""1.外部输入参数"""

module = 'login_moblie' #sheet名称
url = 'https://testchome.seeyon.com'

"""2.根据module获取Sheet"""
logging.info("-------------- Execute TestCases ---------------")
sheet = func.get_excel_sheet(func.filename,  module)

# """3.数据准备"""
# logging.info("-------------- Prepare data through MysqlDB --------------")
# sql = func.get_prepare_sql(sheet)
# func.prepare_data(host=host, user=user, password=password, db=db, sql=sql)

"""4.执行测试用例"""
res = func.run_test(sheet, url)
logging.info("-------------- Get the result ------------ %s", res)