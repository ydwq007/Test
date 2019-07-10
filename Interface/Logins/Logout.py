# -*- coding: utf-8 -*-
#退出登录接口
#y由于PC端是PHP渲染，通过表单提交，但是无法做登录接口测试，故采取移动端的登录接口
import requests,json,re,logging,csv
from bson import json_util
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

#退出接口调用
logout_data = {
        "m":"userMobile",
        "a":"logout"
}
logout_datas = json.dumps(logout_data)
def re_logout():
    #请求接口
    request_logout = requests.post(login_url, data=logout_datas,headers=headers,verify=False) #调用接口（url,参数，类型）#verify=False 跳过认证

    #获取响应数据
    response_logout= json.loads(request_logout.text)

    # print("-----------打印请求数据如下：--------------")
    print(login_url)
    print(json_util.dumps(logout_data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出

    #打印响应结果，以json格式输出
    print("---------打印响应结果：---------------")
    # print(json_util.dumps(response_logout,ensure_ascii=False,indent=4))

    # if "uid" in response_login["data"].keys():
    if response_logout["code"] == 1000:
        print("用户退出登录成功！！！" )
    else:
        message = response_logout["message"]
        print("用户退出登录失败！！！原因为：%s" % message)

if __name__ == "__main__":
    re_logout()