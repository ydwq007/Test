# -*- coding: utf-8 -*-
"""
接口：封装注册接口 - 移动端
创建人：魏奇
更新人：魏奇
更新时间：2019-08-20
说明：由于PC端是PHP渲染，通过表单提交，仅支持手机号注册A类账号
"""

import requests,json,re
from bson import json_util
# from SendCode import randcode
import Logins.SendCode as SendCode
import sys
sys.path.append("../../TestDatas") #跨目录调用需要配置路径
import BasicDatas
# logging.basicConfig(level=logging.DEBUG)



#注册接口地址
register_url = "%s/portal.php" % BasicDatas.test_url_chome


SendCode.sendcode(BasicDatas.mobile, "register") #参数为电话号码，验证码类型，验证码方式（可不传，默认为手机）
randcode = SendCode.sendcode(BasicDatas.mobile, "register") #将获取到的验证码赋值给randcode，返回的是一个列表
data = {
    "m":"userMobileLogin",
    "a":"register",
    "mobile": BasicDatas.mobile,
    "randcode":randcode[0] #手机验证码
}
datas = json.dumps(data) #字典转为json str

#请求接口
request_register = requests.get(register_url, data=datas, headers=BasicDatas.headers, verify=False) #调用接口（url,参数，类型）#verify=False 跳过认证

#获取响应数据
response_register = request_register.text

#利用re正则，获取token
# findall匹配所有符合的返回列表，
# match 和 search 是匹配一次
res_tr = r'"message":"(.*?)"},' #获取message
message = re.findall(res_tr, response_register) #\u4e00-\u9fa5匹配汉字，A-Z匹配大写英文
# form_token = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', response_token) #\u4e00-\u9fa5匹配汉字，A-Z匹配大写英文

# print("-----------打印请求数据如下：--------------")
print(register_url)
print(json_util.dumps(data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出

#打印响应结果，以json格式输出
print("---------打印响应结果：---------------")
# print(response_register)

if '"code":1000' in response_register:
# if "uid" in response_register["data"].keys():
    print("手机号%s，账号注册成功！！！" % BasicDatas.mobile)
else:
    print("手机号%s，账号注册失败！！！原因为：%s" % (BasicDatas.mobile, message))
