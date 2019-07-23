# -*- coding: utf-8 -*-
"""
接口：封装发送手机或者邮箱验证码接口 - 移动端
创建人：魏奇
更新人：魏奇
更新时间：2019-07-09
说明：由于PC端是PHP渲染，通过表单提交，仅支持手机号注册A类账号
"""

import requests,json,re,logging,csv,sys
from bson import json_util
sys.path.append(r'..\TestDatas') #跨目录调用需要配置路径
from BasicDatas import mobile
# logging.basicConfig(level=logging.DEBUG)


#测试环境
environment1 = "https://testchome.seeyon.com" #测试环境

#接口地址
send_url = "%s/portal.php" % environment1

#信息头
headers = {
    "Content-Type": "application/json"
    #     # "Connection": "keep-alive"
    # "Accept-Encoding": "gzip, deflate, br",
    # "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}
def sendcode(param,sendby = "login",type = "mobile"): #参数为参数（手机或邮箱），验证码类型（可不传，默认为登录），验证码方式（可不传，默认为手机）
    #参数
    # sendBy = sendby
    # type = type
    # param = param
    data = {
        "m":"code",
        "a":"sendCode",
        "sendBy":sendby, #验证码类型,支持 register/findPass/rebind/rebindOld/login
        "type":type, #验证方式mobile / email
        "param":param, #手机号或者邮箱
        "is_mobile":"1", #是否移动端
        "no_use_img_code":"1" #是否使用图形验证码,0：使用，1：不使用
    }
    datas = json.dumps(data) #字典转为json str

    #请求接口
    request_send = requests.get(send_url,data=datas,headers=headers,verify=False) #调用接口（url,参数，类型）#verify=False 跳过认证

    #获取响应数据
    response_send = request_send.text
    # print(type(response_send))
    #利用re正则，获取token
    # findall匹配所有符合的返回列表，
    # match 和 search 是匹配一次
    res_tr1 = r'"randcode":"(.*?)"},' #获取验证码
    res_tr2 = r'"message":"(.*?)"},' #获取message
    randcode = re.findall(res_tr1, response_send) #\u4e00-\u9fa5匹配汉字，A-Z匹配大写英文
    message = re.findall(res_tr2, response_send) #\u4e00-\u9fa5匹配汉字，A-Z匹配大写英文
    # form_token = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', response_token) #\u4e00-\u9fa5匹配汉字，A-Z匹配大写英文

    # print("-----------打印请求数据如下：--------------")
    print(send_url)
    print(json_util.dumps(data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出

    #打印响应结果，以json格式输出
    print("---------打印响应结果：---------------")
    # print(response_send)
    # print(randcode[0])
    if '"code":1000' in response_send:
        # if "randcode" in response_send["data"].keys():
        print("获取验证码成功！！！")
        print("验证码为%s" % randcode[0])
        return randcode
    else:
        print("获取验证码失败！！！，原因为：%s" % message[0])

if __name__ == "__main__":
    try:
        sendcode(mobile)
    except TypeError:
        print("验证码次数超过最多限制")
    except IndexError:
        print("序列中没有此索引(index)")

