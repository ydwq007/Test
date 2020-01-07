# -*- coding: utf-8 -*-
"""
接口：封装登录接口 - 移动端
创建人：魏奇
更新人：魏奇
更新时间：2019-07-08
说明：由于PC端是PHP渲染，通过表单提交，但是无法做登录接口测试，故采取移动端的登录接口
"""

import requests,json, sys
import Logins.SendCode as SendCode
# import unittest
# from unittest import TestCase
sys.path.append('../../TestDatas') #跨目录调用需要配置路径
from bson import json_util
import BasicDatas
# # logging.basicConfig(level=logging.DEBUG)

#基本参数：
#登录接口地址
# login_url = "%s/portal.php" % BasicDatas.test_url_chome
#选择登录方式
Login_mode = 1 #1代表密码登录，否则代表验证码登录

#封装登录接口
def login_mobile(host,username,password,mobile=""):

    #设置接口参数
    if Login_mode == 1:
        #密码登录
        login_data = {
            "m":"userMobileLogin",
            "a":"login",
            "username":username,
            "password":password,
            "account_type":"1" #1: A类（商城）  2: B类（云工厂）
        }
        login_datas = json.dumps(login_data) #json.dumps()用于将字典形式的数据转化为json字符串
    else:
        #验证码登录
        # SendCode.sendcode(mobile) #参数为电话号码，验证码类型（可不传，默认为登录），验证码方式（可不传，默认为手机）
        randcode = SendCode.sendcode(mobile) #将获取到的验证码赋值给randcode，返回的是一个列表
        login_data = {
            "m":"userMobileLogin",
            "a":"loginByCode",
            "mobile":mobile,
            "randcode":randcode[0]
        }
        login_datas = json.dumps(login_data) ##json.dumps()用于将字典形式的数据转化为json字符串

    #测试地址
    login_url = "%s/portal.php" % host

    #调用请求
    request_login = requests.post(login_url, data=login_datas, headers=BasicDatas.headers, verify=False) #调用接口（url,参数，类型）#verify=False 跳过认证
    #获取响应数据
    response_login= json.loads(request_login.text) #json.loads()用于将字符串形式的数据转化为字典

    #调试时打印
    # print("-----------打印请求数据如下：--------------")
    print("登录地址为：%s" % login_url)
    # print(login_datas)
    print("登录请求参数为：\n%s" % json_util.dumps(login_data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出

    print("---------打印响应结果：---------------")
    print("登录响应结果为：\n%s" % json_util.dumps(response_login,ensure_ascii=False,indent=4)) #打印响应数据，以json格式输出
    # if "uid" in response_login["data"].keys(): #通过字段判断
    if response_login["code"] == 1000: #通过响应码判断
        #分解成功情况
        token = response_login["data"]["token"]["access_token"]
        uid = response_login["data"]["uid"]
        Authorization = "bearer %s" % token
        if Login_mode == 1:
            print("username为%s，uid为%s的用户登录成功！！！token为：%s" % (username,uid,token))
        else:
            print("mobile为%s，uid为%s的用户登录成功！！！token为：%s" % (mobile,uid,token))
        return True,token,uid,Authorization
    else:
        #分解失败情况
        message = response_login["message"]
        if Login_mode == 1:
            if username == "":
                print("username为空的用户登录失败！！！原因为：%s" % message)
            else:
                print("username为%s的用户登录失败！！！原因为：%s" % (username,message))
        else:
            print("mobile为%s的用户登录失败！！！原因为：%s" % (mobile,message))
        return False,message

if __name__ == "__main__":
    # login_mobile() #调用接口
    login_mobile(BasicDatas.test_url_chome,"gold002","123456",15982286537) #调用接口
