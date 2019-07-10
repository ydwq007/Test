# -*- coding: utf-8 -*-
#登录相关接口，包含登录，退出，登录校验
#y由于PC端是PHP渲染，通过表单提交，但是无法做登录接口测试，故采取移动端的登录接口
import requests,json,re,logging,csv
from bson import json_util
import SendCode
from BasicDatas import mobile,usernames,password
# logging.basicConfig(level=logging.DEBUG)

#信息头
headers = {
    "Content-Type": "application/json"
    #     # "Connection": "keep-alive"
    # "Accept-Encoding": "gzip, deflate, br",
    # "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}

#测试环境
environment1 = "https://testchome.seeyon.com" #测试环境

#登录接口地址
login_url = "%s/portal.php" % environment1

#登录接口调用
#选择登录方式
Login_mode = 2 #1代表密码登录，否则代表验证码登录

def re_login():

    if Login_mode == 1:
        #密码登录
        login_data1 = {
            "m":"userMobileLogin",
            "a":"login",
            "username":usernames[0],
            "password":password,
            "account_type":"1" #1: A类（商城）  2: B类（云工厂）
        }
        login_datas = json.dumps(login_data1)
    else:
        #验证码登录
        SendCode.sendcode(mobile) #参数为电话号码，验证码类型（可不传，默认为登录），验证码方式（可不传，默认为手机）
        randcode = SendCode.sendcode(mobile) #将获取到的验证码赋值给randcode，返回的是一个列表
        login_data2 = {
            "m":"userMobileLogin",
            "a":"loginByCode",
            "mobile":mobile,
            "randcode":randcode[0]
        }
        login_datas = json.dumps(login_data2)
    #请求接口
    request_login = requests.post(login_url, data=login_datas,headers=headers,verify=False) #调用接口（url,参数，类型）#verify=False 跳过认证

    #获取响应数据
    response_login= json.loads(request_login.text)

    # print("-----------打印请求数据如下：--------------")
    print(login_url)
    print(login_datas)
    # print(json_util.dumps(data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出

    #打印响应结果，以json格式输出
    print("---------打印响应结果：---------------")
    # print(json_util.dumps(response_login,ensure_ascii=False,indent=4))

    # if "uid" in response_login["data"].keys():
    if response_login["code"] == 1000:
        token = response_login["data"]["token"]["access_token"]
        if Login_mode == 1:
            print("username为%s的用户登录成功！！！token为：%s" % (usernames[0],token))
        else:
            print("mobile为%s的用户登录成功！！！token为：%s" % (mobile,token))

    else:
        message = response_login["message"]
        if Login_mode == 1:
            print("username为%s的用户登录失败！！！原因为：%s" % (usernames[0],message))
        else:
            print("mobile为%s的用户登录失败！！！原因为：%s" % (mobile,message))

if __name__ == "__main__":
    try:
        re_login()
        # SendCode.sendcode(mobile) #参数为电话号码，验证码类型（可不传，默认为登录），验证码方式（可不传，默认为手机）
        # randcode = SendCode.sendcode(mobile) #将获取到的验证码赋值给randcode，返回的是一个列表
    except TypeError:
        print("验证码次数超过最多限制,SendCode接口报错")
    except IndexError:
        print("序列中没有此索引(index),SendCode接口报错")


