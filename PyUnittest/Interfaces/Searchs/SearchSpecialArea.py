# -*- coding: utf-8 -*-
#专区搜索接口
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
environment1 = "https://vprodcloud.seeyon.com" #测试环境

#登录接口地址
login_url = "%s/rest/search/searchSpecialArea" % environment1

def area_search(keywords):
    area_data = {
        "keywords":keywords
    }
    area_datas = json.dumps(area_data)
    #调用接口
    request_areasearch = requests.post(login_url, data=area_datas,headers=headers,verify=False) #调用接口（url,参数，类型）#verify=False 跳过认证

    #获取响应数据
    response_areasearch= json.loads(request_areasearch.text)

    # print("-----------打印请求数据如下：--------------")
    print(login_url)
    print(area_data)
    # print(json_util.dumps(data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出

    #打印响应结果，以json格式输出
    print("---------打印响应结果：---------------")
    # print(json_util.dumps(response_areasearch,ensure_ascii=False,indent=4))
    if response_areasearch["code"] == "1000":
        total_count = response_areasearch["data"]["total_count"]
        print("专区搜索成功！！！数据共%s条" % total_count )
        print(json_util.dumps(response_areasearch["data"],ensure_ascii=False,indent=4))
    else:
        message = response_areasearch["message"]
        print("专区搜索失败！！！原因为：%s" % message)

if __name__ == "__main__":
    area_search()