# -*- coding: utf-8 -*-
#基础数据
"""
接口：基础数据准备
创建人：魏奇
更新人：魏奇
更新时间：2019-08-21
"""

#正常登陆的用户账号数据
usernames = ["gold002","test01"] #正确账号
password = "123456" #默认密码为123456
mobile = "13111111114"

#登录接口测试数据
#参数用列表保存，第一个值为案例的内容，第三
parameter_login = [["用户名密码均正确的情况","gold002","123456",True],["密码错误的情况","gold002","1234561",False],["密码为空的情况","gold002","",False],
             ["用户名为空的情况","","123456",False],["用户名错误的情况","gold101","123456",False]]

#环境
#类生产
vprod_mall = "https://vprodcloud.seeyon.com"
vprod_chome = "https://vprodchome.seeyon.com"
vprod_manager = "https://vprodcmanager.seeyon.com"

#测试
test_mall = "https://testcloud.seeyon.com"
test_chome = "https://testchome.seeyon.com"
test_manager = "https://testcmanager.seeyon.com"

#测试地址
test_url_mall = test_mall
test_url_chome = test_chome
test_url_manager = test_manager

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

