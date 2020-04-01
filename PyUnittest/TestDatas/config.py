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
vprod_mall = "https://vprodcloud.seeyon.com"
vprod_chome = "https://vprodchome.seeyon.com"
vprod_manager = "https://vprodcmanager.seeyon.com"

#测试
test_mall = "https://testcloud.seeyon.com"
test_chome = "https://testchome.seeyon.com"
test_manager = "https://testcmanager.seeyon.com"

#接口测试
citest_mall = "https://citestcloud.seeyon.com"
citest_chome = "https://citestchome.seeyon.com"
citest_manager = "https://citestcmanager.seeyon.com"

#测试地址
test_url_mall = test_mall
test_url_chome = test_chome
test_url_manager = test_manager

#信息头
#信息头
pc_headers = {
    "Content-Type": "application/json",
    "Connection":"keep-alive",
    "Cookie": "",
}
mobile_headers = {
    "Content-Type": "application/json",
    "Connection":"keep-alive",
    "Cookie": "",
    "Authorization":""
}
headers = {
    "Content-Type": "application/json",
    "Connection":"keep-alive"
}

#正常登陆的用户账号数据
usernames = ["gold002","15982280117"] #正确账号
password = "123456" #默认密码为123456
mobile = "13111111114"

# 纯A类账号登录参数
aloneA = {
    "m": "LoginCloud",
    "a": "login",
    "account_type": 1,
    "username": "15982280117",
    "password": "123456"
}
# 经销商账号登录
dealer = {
        "m": "LoginCloud",
        "a": "login",
        "account_type": 2,
        "username": "happy01",
        "password": "123456"
}

dealer1 = {
    "m": "LoginCloud",
    "a": "login",
    "account_type": 2,
    "username": "gold002",
    "password": "123456"
}

# 无证书账号
dealer2 = {
    "m": "LoginCloud",
    "a": "login",
    "account_type": 2,
    "username": "happy02",
    "password": "123456"
}

# 证书异常账号
dealer3 = {
    "m": "LoginCloud",
    "a": "login",
    "account_type": 2,
    "username": "happy03",
    "password": "123456"
}

# 未绑定加密狗
dealer4 = {
    "m": "LoginCloud",
    "a": "login",
    "account_type": 2,
    "username": "happy04",
    "password": "123456"
}

# 通狗下单
dealer5 = {
    "m": "LoginCloud",
    "a": "login",
    "account_type": 2,
    "username": "happy05",
    "password": "123456"
}

# 无经销商单位
dealer6 = {
    "m": "LoginCloud",
    "a": "login",
    "account_type": 2,
    "username": "happy06",
    "password": "123456"
}

# 试用狗下单
dealer7 = {
    "m": "LoginCloud",
    "a": "login",
    "account_type": 2,
    "username": "happy07",
    "password": "123456"
}

# 用户中心登录

# 创建普通订单
normal_order = {
        "user_id": "15792269950270000",
        "goods_sku_list": "3094:1",
        "buyer_org_id": "4821377249100515603",
        "service_org_id": "-7422902346933186598",
        "company_name": "有证书有经销商",
        "contact_name": "user904698",
        "contact_phone": "15982280117",
        "order_tag": "",
        "coupon_id": "",
        "memo": "接口测试数据"
}

# 创建0元订单
zero_order = {
    "user_id": "15792269950270000",
    "goods_sku_list": "3039:1",
    "buyer_org_id": "4821377249100515603",
    "service_org_id": "-7422902346933186598",
    "company_name": "有证书有经销商",
    "contact_name": "user904698",
    "contact_phone": "15982280117",
    "order_tag": "",
    "coupon_id": "",
    "memo": "接口测试数据"
}


#登录接口测试数据
#参数用列表保存，第一个值为案例的内容，第三
parameter_login = [["用户名密码均正确的情况","gold002","123456",True],["密码错误的情况","gold002","1234561",False],["密码为空的情况","gold002","",False],
                   ["用户名为空的情况","","123456",False],["用户名错误的情况","gold101","123456",False]]

# 测试用例
# filepath = "../../TestDatas/接口测试用例.xlsx"
filepath = "../../Experiment/Other/接口测试用例.xlsx"