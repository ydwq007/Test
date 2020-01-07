# -*- coding: utf-8 -*-
"""
接口：封装登录前获取token接口 -PC端
创建人：魏奇
更新人：魏奇
更新时间：2019-08-20
说明：由于PC端是PHP渲染，通过表单提交，但是无法做登录接口测试，故采取移动端的登录接口
"""

import requests,re
# logging.basicConfig(level=logging.DEBUG)
import sys
sys.path.append(r"D:\IdeaProjects\seeyon\PyUnittest\TestDatas") #跨目录调用需要配置路径
import BasicDatas

def getToken():

    #登录页面
    login_token = "%s/portal.php?m=user&a=login" % BasicDatas.test_url_chome

    #请求接口
    request_token = requests.get(login_token, headers=BasicDatas.headers, verify=False) #调用接口（url,参数，类型）#verify=False 跳过认证

    #获取响应数据
    response_token = request_token.text

    #利用re正则，获取token
    # findall匹配所有符合的返回列表，
    # match 和 search 是匹配一次
    res_tr = r'id="form_token" value="(.*?)"/>'
    form_token = re.findall(res_tr, response_token) #\u4e00-\u9fa5匹配汉字，A-Z匹配大写英文
    # form_token = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', response_token) #\u4e00-\u9fa5匹配汉字，A-Z匹配大写英文

    #打印响应结果
    print("---------打印接口响应结果：---------------")
    # print(response_token) #打印整个响应结果
    print(form_token) #打印form_token
    return form_token

if __name__ == "__main__":
    getToken()

