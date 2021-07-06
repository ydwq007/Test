# -*- coding: utf-8 -*-
# 基础数据
"""
接口：配置基础数据
创建人：魏奇
创建时间：2019-07-16
"""

# 数据库配置
# 测试
test_cmall_db = {
    "host": "172.31.10.8",
    "port": 3306,
    "username": "cmall",
    "password": "6eb6a4d!ce450b7e96Ge7630c",
    "dbname": "cmall"
}

test_chome_db = {
    "host": "172.31.10.8",
    "port": 3306,
    "username": "chome",
    "password": "Bd383975f781d1e25d7a94!26",
    "dbname": "chome"
}

test_usercenter_db = {
    "host": "172.31.10.8",
    "port": 3306,
    "username": "usercenter",
    "password": "6dfa6P3d27fe42f96f8T1268!",
    "dbname": "usercenter"
}


# 测试环境配置
# 测试环境
test_mall = "https://testcloud.seeyon.com"
test_chome = "https://testchome.seeyon.com"
test_manager = "https://testcmanager.seeyon.com"
test_file = "https://testfilestorage.seeyon.com"
test_order = "https://testorder.seeyon.com"
test_internal = "http://cloud.test.internal.seeyon.site"
test_dhome = "https://testdhome.seeyoncloud.com"

# CI环境
citest_mall = "https://citestcloud.seeyoncloud.com"
citest_chome = "https://citestchome.seeyoncloud.com"
citest_manager = "https://citestcmanager.seeyoncloud.com"
citest_file = "https://citestfilestorage.seeyon.com"
citest_order = "https://testorder.seeyon.com"
citest_internal = "http://cloud.citest.internal.seeyon.site"

# 邮件接收地址
email_adress_CI = ["weiqi@seeyon.com", "775636762@qq.com", "596123007@qq.com", "664785288@qq.com", "judy_ning@163.com"]  # CITEST环境
email_adress_TEST = ["weiqi@seeyon.com", "775636762@qq.com"]  # 调试用
email_adress_ALL = ["weiqi@seeyon.com", "775636762@qq.com", "lhhy528@163.com", "991804679@qq.com", "1404846503@qq.com"]

# 默认信息头
headers = {
    "Content-Type": "application/json",
    "Connection": "keep-alive",
    "X-TENANT-CODE": "cloud_operation"
}

# 默认账号密码
accountp = {
    "username": "happy01",
    "password": "123456"
}
# 用例文件
filepath_test_wq = "../../TestDatas/云服务_接口测试用例-魏奇.xlsx"
filepath_test_dhy = "../../TestDatas/dhome_接口测试用例_杜海燕.xlsx"
filepath_test_all = "../../TestDatas/接口测试用例_TESTALL.xlsx"
filepath_test_wjj = "../../TestDatas/小程序测试用例-吴京津.xlsx"


filepath_ci_wq = "../../TestDatas/接口测试用例-魏奇-CI.xlsx"
filepath_ci_all = "../../TestDatas/接口测试用例_CIALL.xlsx"




# 通过配置区分获取运行环境的基本数据
config_sys = 1  # 1为测试环境，2为CITEST环境
if config_sys == 1:

    # 测试地址
    test_url_mall = test_mall
    test_url_chome = test_chome
    test_url_manager = test_manager
    test_url_file = test_file
    test_url_order = test_order
    test_url_internal = test_internal
    test_url_dhome = test_dhome
    # 用例文件
    file_path = filepath_test_wq
    # 邮件地址
    email_adress = email_adress_TEST

elif config_sys == 2:

    # 测试地址
    test_url_mall = citest_mall
    test_url_chome = citest_chome
    test_url_manager = citest_manager
    test_url_file = citest_file
    test_url_order = citest_order
    test_url_internal = citest_internal
    # 用例文件
    filepath = filepath_ci_wq
    # 邮件地址
    email_adress = email_adress_CI

else:
    print("config_sys配置参数错误")