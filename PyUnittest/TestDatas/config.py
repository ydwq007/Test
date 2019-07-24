# -*- coding: utf-8 -*-
#基础数据
"""
接口：配置基础数据
创建人：魏奇
更新人：魏奇
更新时间：2019-07-16
"""

#数据库配置
#测试
test_cmall_db = {
    "host":"172.31.10.8",
    "port":3306,
    "username":"cmall",
    "password":"6eb6a4d!ce450b7e96Ge7630c",
    "dbname":"cmall"
}

test_chome_db = {
    "host":"172.31.10.8",
    "port":3306,
    "username":"chome",
    "password":"Bd383975f781d1e25d7a94!26",
    "dbname":"chome"
}

test_usercenter_db = {
    "host":"172.31.10.8",
    "port":3306,
    "username":"usercenter",
    "password":"6dfa6P3d27fe42f96f8T1268!",
    "dbname":"usercenter"
}

#类生产

#测试环境配置
#类生产
vprod_cmall = "https://vprodcloud.seeyon.com"
vprod_chome = "https://vprodchome.seeyon.com"
vprod_manager = "https://vprodcmanager.seeyon.com"

#测试
test_cmall = "https://testcloud.seeyon.com"
test_chome = "https://testchome.seeyon.com"
test_manager = "https://testcmanager.seeyon.com"

#信息头
headers = {
    "Content-Type": "application/json"
    #     # "Connection": "keep-alive"
    # "Accept-Encoding": "gzip, deflate, br",
    # "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}