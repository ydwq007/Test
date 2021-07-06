# -*- coding: utf-8 -*-
"""
接口：将基础接口按照业务进行封装
创建人：魏奇
创建时间：2021-04-02 17:10
描述：
"""
import requests
import json
import re
import sys
sys.path.append("../../TestDatas")
import config, Basic_Interface
from bson import json_util


# 验证码登录
def login_code(url, headers, mobile, smstype="LOGIN", imgCode="54"):
    """
    :param url: 域名
    :param headers：请求头
    :param mobile：手机号
    :param smstype：类型，默认登录
    :param imgCode: 验证码

    """
    # 获取图形验证码
    captcha = Basic_Interface.get_captcha_image(url, headers)
    # print(json_util.dumps(captcha, ensure_ascii=False, indent=4))

    codekey = captcha[0]

    sms_data = {
        "account": mobile,
        "imgCode": "54",
        "imgCodeKey": codekey,
        "business": smstype,
        "channel": "SMS"
    }

    smscode = Basic_Interface.get_SmsCode(url, headers, sms_data)
    # print(json_util.dumps(smscode, ensure_ascii=False, indent=4))

    # 登录
    login_data = {
        "code": smscode,
        "codeKey": "",
        "codeResult": "",
        "mobile": mobile,
        "password": "",
        "username": ""
    }

    login = Basic_Interface.cloud_login_auth(url, headers, login_data)
    # print(json_util.dumps(login, ensure_ascii=False, indent=4))

    token = login[0]
    uid = login[1]

    return token, uid

# 用户名密码登录
def login_password(url, headers, username, password, imgCode="54"):

    """
    :param url: 域名
    :param headers：请求头
    :param username：用户名
    :param password：密码
    :param imgCode: 验证码

    """
    # 获取图形验证码
    captcha = Basic_Interface.get_captcha_image(url, headers)
    # print(json_util.dumps(captcha, ensure_ascii=False, indent=4))

    codekey = captcha[0]

    # 登录
    login_data = {
        "code": "",
        "codeKey": codekey,
        "codeResult": imgCode,
        "mobile": "",
        "password": password,
        "username": username
    }

    login = Basic_Interface.cloud_login_auth(url, headers, login_data)
    # print(json_util.dumps(login, ensure_ascii=False, indent=4))

    token = login[0]
    uid = login[1]

    return token, uid

# 注册
def account_register(url, headers, mobile, smstype="REGISTER", imgCode="54"):
    """
    :param url: 域名
    :param headers：请求头
    :param mobile：手机号
    :param smstype：类型，默认登录
    :param imgCode: 验证码

    """
    # 获取图形验证码
    captcha = Basic_Interface.get_captcha_image(url, headers)
    # print(json_util.dumps(captcha, ensure_ascii=False, indent=4))

    codekey = captcha[0]

    # 获取短信验证码
    sms_data = {
        "imgCodeKey": codekey,
        "imgCode": imgCode,
        "account": mobile,
        "business": smstype,
        "channel": "SMS"
    }

    smscode = Basic_Interface.get_SmsCode(url, headers, sms_data)
    # print(json_util.dumps(smscode, ensure_ascii=False, indent=4))

    # 注册
    register_data = {
        "busOrgId": "",
        "codeKey": codekey,
        "imgCode": imgCode,
        "invStyle": "",
        "invType": "",
        "invUid": "",
        "mobile": mobile,
        "orgId": "",
        "randcode": smscode
    }

    register = Basic_Interface.cloud_register(url, headers, register_data)
    # print(json_util.dumps(register, ensure_ascii=False, indent=4))

    token = register[0]
    uid = register[1]

    return token, uid

# 更新请求头，新增token
def updata_header(url, headers, login_data, system=1, login_style=1, Tenant_identification="cloud_operation"):
    """
    :param url: 域名
    :param headers：请求头
    :param login_data：登录参数
    :param system：登录系统，默认1商城登录，2基础服务登录
    :param login_style：登录方式，默认1用户名密码，2手机号验证码

    """
    # 商城登录
    if system == 1:
        # data = json.loads(login_data)
        # 用户名密码登录
        if login_style == 1:
            username = login_data["username"]
            password = login_data["password"]
            login_result = login_password(url, headers, username, password)
        # 手机验证码登录
        else:
            mobile = login_data["mobile"]
            login_result = login_code(url, headers, mobile)
    # 基础服务登录
    elif system == 2:
        login_result = Basic_Interface.dhome_login_auth(url, headers, login_data)

    # print(login_result)
    header_data = {
        "Content-Type": "application/json",
        "Connection": "keep-alive",
        "X-TENANT-CODE": Tenant_identification,
        "Authorization": "%s" % login_result[0]
    }
    new_headers = json.dumps(header_data)
    return new_headers



if __name__ == "__main__":
    re_url = config.test_url_mall
    dhome_url = config.test_url_dhome
    headers = config.headers
    mobile_1 = "15982282086"
    mobile_2 = "15904060013"
    username = "happy01"
    password = "123456"
    login_data = {
        "username": "dhome_admin",
        "password": "123456",
        "mobile": "",
        "email": ""
    }

    # print(login_code(re_url, headers, mobile_1)[0])
    print(login_password(re_url, headers, username, password)[0])
    # print(account_register(re_url, headers, mobile_2))
    # print(login_data)
    # print(type(login_data))
    # print(updata_header(dhome_url, headers, login_data, system=2, login_style=1))

