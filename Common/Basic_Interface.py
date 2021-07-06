# -*- coding: utf-8 -*-
"""
接口：构造接口测试需要的基础接口
创建人：魏奇
创建时间：2021-04-02 14:30
描述：
"""
import logging

import requests
import json
import re
import sys
sys.path.append("../../TestDatas")
import config
from bson import json_util
import urllib3
urllib3.disable_warnings()


# 获取图形验证码，/captcha/image/get
def get_captcha_image(url, headers):
    """
    :param url: 访问域名
    :param headers: 信息头
    """
    captcha_image_url = "%s/adminservice/captcha/image/get" % url
    # print(captcha_image_url)

    try:
        captcha_image_request = requests.request("GET", url=captcha_image_url, headers=headers, verify=False)
        captcha_image_result = json.loads(captcha_image_request.text)
        # print(json_util.dumps(captcha_image_result, ensure_ascii=False, indent=4))

        if captcha_image_request.status_code == 200:
            code_key = captcha_image_result["data"]["codeKey"]
            image = captcha_image_result["data"]["image"]
        else:
            print("图形验证码获取失败，原因：%s" % captcha_image_result["message"])
            code_key = None
            image = None
    except Exception as errs:
        logging.exception("出现问题")
        raise errs

    return code_key, image

# 获取短信验证码，/commonapi/auth/sendSmsCode
def get_SmsCode(url, headers, sms_data):
    """
    :param url: 访问域名
    :param headers: 信息头
    :param sms_data:请求参数
    sms_data：
    {
    :param account: 账号：手机号或者邮箱
    :param business: 业务：LOGIN(登录)/REGISTER(注册)/BIND(绑定)/FORGET(忘记密码)/COMMON(普通验证/MERGE(合并账号))
    :param channel: 渠道：MOBILE/EMAIL/INBOX
    :param checkExist: 检测账号是否存在
    :param checkUse: 检测账号是否被使用
    :param imgCode: 图形验证码
    :param imgCodeKey: 图形验证码KEY
    :param template: 发送模板
    }
    """
    SmsCode_url = "%s/adminservice/code/send" % url
    # print(SmsCode_url)
    datas = json.dumps(sms_data)
    # print(datas)

    try:
        SmsCode_request = requests.post(url=SmsCode_url, data=datas, headers=headers, verify=False)
        SmsCode_result = json.loads(SmsCode_request.text)
        # print(json_util.dumps(SmsCode_result, ensure_ascii=False, indent=4))

        if SmsCode_request.status_code == 200:
            code = SmsCode_result["data"]["verifyCode"]
        else:
            print("短信验证码获取失败，原因：%s" % SmsCode_result["message"])
            code = None
    except Exception as errs:
        logging.exception("出现问题")
        raise errs

    return code



# 获取云商城登录授权，/commonapi/auth/login
def cloud_login_auth(url, headers, login_data):
    """
    :param url: 域名
    :param headers: 信息头
    :param login_data: 请求参数
    login_data：
    {
    :param username: 用户名
    :param password: 密码
    :param codeResult: 图形验证码结果
    :param mobile: 手机号
    :param codeKey: 图形验证码key
    :param code: 短信验证码
    }
    """
    login_auth = "%s/adminservice/auth/login" % url
    # print(login_auth)
    datas = json.dumps(login_data)
    # print(datas)

    try:
        login_auth_request = requests.post(url=login_auth, data=datas, headers=headers, verify=False)
        login_auth_result = json.loads(login_auth_request.text)
        # print(json_util.dumps(login_auth_result, ensure_ascii=False, indent=4))

        if login_auth_request.status_code == 200:
            token = login_auth_result["data"]["token"]
            uid = login_auth_result["data"]["user"]["id"]
        else:
            print("登录失败，原因：%s" % login_auth_result["message"])
            token = None
            uid = None
    except Exception as errs:
        logging.exception("出现问题")
        raise errs

    return token, uid

# 云商城注册新账号，/commonapi/auth/register
def cloud_register(url, headers, register_data):
    """
    :param url: 域名
    :param headers：请求头
    :param register_data：注册参数
    register_data：
    {
    :param busOrgId：邀请人商家单位ID
    :param codeKey：图像验证码key
    :param imgCode：图形验证码
    :param invStyle：邀请方式：0默认二维码；1微信分享；2QQ分享；3复制链接
    :param invType：邀请类型：0默认二维码邀请；1商品分享；2案例分享；4专区分享；5活动分享
    :param invUid：邀请人ID
    :param mobile：手机号
    :param orgId：邀请人单位ID
    :param randcode：短信验证码
    }
    """
    register_url = "%s/adminservice/auth/register" % url
    # print(register_url)
    datas = json.dumps(register_data)
    # print(datas)

    try:
        register_request = requests.post(url=register_url, data=datas, headers=headers, verify=False)
        register_result = json.loads(register_request.text)
        # print(json_util.dumps(register_result, ensure_ascii=False, indent=4))

        if register_request.status_code == 200:
            token = register_result["data"]["token"]
            uid = register_result["data"]["user"]["id"]
            mobile = register_result["data"]["user"]["mobile"]
        else:
            print("注册失败，原因：%s" % register_result["message"])
            token = None
            uid = None
            mobile = None
    except Exception as errs:
        logging.exception("出现问题")
        raise errs

    return token, uid, mobile

# 获取dhome登录授权，/dhome/auth/login
def dhome_login_auth(url, headers, login_data):
    """
    :param url: 域名
    :param headers: 信息头
    :param login_data: 请求参数
    login_data：
    {
    :param username: 用户名
    :param password: 密码
    :param mobile: 手机号
    :param email: 邮箱
    }
    """
    login_auth = "%s/dhome/auth/login" % url
    # print(login_auth)
    datas = json.dumps(login_data)
    # print(datas)

    try:
        login_auth_request = requests.post(url=login_auth, data=datas, headers=headers, verify=False)
        login_auth_result = json.loads(login_auth_request.text)
        # print(json_util.dumps(login_auth_result, ensure_ascii=False, indent=4))

        if login_auth_request.status_code == 200:
            token = login_auth_result["data"]["token"]
            uid = login_auth_result["data"]["uid"]
        else:
            print("登录失败，原因：%s" % login_auth_result["message"])
            token = None
            uid = None
    except Exception as errs:
        logging.exception("出现问题")
        raise errs

    return token, uid

# 通过加狗号获取单位信息
def org_detail(url, headers, org_data):
    """
    :param org_data: 请求参数
    org_data:
    {
    :param dogNo: 加密狗号
    :param productTypeArray:
    }
    :param header: 请求头
    :param url: 域名
    """

    org_detail_url = "%s/dhome/biz/findUcOrgsByDogNo" % url
    # print(org_detail_url)

    datas = json.dumps(org_data)
    # print(datas)

    try:
        org_detail_request = requests.post(url=org_detail_url, data=datas, headers=headers, verify=False)
        org_detail_result = json.loads(org_detail_request.text)
        # print(json_util.dumps(org_detail_result, ensure_ascii=False, indent=4))

        if org_detail_request.status_code == 200:
            customName = org_detail_result["customName"]
            dogNo = org_detail_result["dogNo"]
            orgId = org_detail_result["orgId"]

        else:
            print("通过狗号获取单位信息失败，原因：%s" % org_detail_result["message"])
            customName = None
            dogNo = None
            orgId = None
    except Exception as errs:
        logging.exception("出现问题")
        raise errs

    return customName, dogNo, orgId




if __name__ == "__main__":
    re_url = config.test_url_mall
    dhome_url = config.test_url_dhome
    headers = config.headers
    captcha = get_captcha_image(re_url, headers)
    codekey_1 = captcha[0]
    mobile = "15982282086"
    # sms_data_reg = {
    #     "account": mobile,
    #     "business": "REGISTER",
    #     "channel": "SMS",
    #     "imgCode": "54",
    #     "imgCodeKey": codekey_1
    # }
    # sms_data_login = {
    #     "account": mobile,
    #     "business":"LOGIN",
    #     "channel":"SMS",
    #     "imgCode": "54",
    #     "imgCodeKey": codekey_1
    # }

    # sms_data_login = {
    #     "account":"15082435789",
    #     "imgCode":"54",
    #     "imgCodeKey":codekey_1,
    #     "business":"LOGIN",
    #     "channel":"SMS"
    # }
    #
    # auth_code = get_SmsCode(re_url, headers, sms_data_login)
    # code = auth_code
    login_data_ps = {
        "code": "",
        "codeKey": codekey_1,
        "codeResult": "54",
        "mobile": "",
        "password": "123456",
        "username": "happy01"
    }
    # login_data_code = {
    #     "code": code,
    #     "codeKey": "",
    #     "codeResult": "",
    #     "mobile": mobile,
    #     "password": "",
    #     "username": ""
    # }
    print(cloud_login_auth(re_url, headers, login_data_ps))
    # print(cloud_login_auth(re_url, headers, login_data_code))
    # register_data = {
    #     "busOrgId": "",
    #     "codeKey": codekey_1,
    #     "imgCode": "54",
    #     "invStyle": "",
    #     "invType": "",
    #     "invUid": "",
    #     "mobile": mobile,
    #     "orgId": "",
    #     "randcode": auth_code
    # }
    # login_data = {
    #     "username": "dhome_admin",
    #     "password": "123456",
    #     "mobile": "",
    #     "email": ""
    # }
    # print(cloud_register(re_url, headers, register_data))
    # print(dhome_login_auth(dhome_url, headers, login_data))
    # org_data = {
    #     "dogNo": "210101",
    #     "productTypeArray": ""
    # }
    # org_detail(dhome_url, headers, org_data)

