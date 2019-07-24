# -*- coding: utf-8 -*-
"""
接口：封装商品搜索接口 - 移动端
创建人：魏奇
更新人：魏奇
更新时间：2019-07-08
说明：
"""

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
login_url = "%s/rest/search/searchGoods" % environment1

def goods_search(keywords):
    goods_data = {
        "keywords":keywords
    }
    goods_datas = json.dumps(goods_data)
    #调用接口
    request_goodssearch = requests.post(login_url, data=goods_datas,headers=headers,verify=False) #调用接口（url,参数，类型）#verify=False 跳过认证

    #获取响应数据
    response_goodssearch= json.loads(request_goodssearch.text)

    # print("-----------打印请求数据如下：--------------")
    print(login_url)
    print(goods_data)
    # print(json_util.dumps(data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出

    #打印响应结果，以json格式输出
    print("---------打印响应结果：---------------")
    # print(json_util.dumps(response_goodssearch,ensure_ascii=False,indent=4))
    if response_goodssearch["code"] == "1000":
        total_count = response_goodssearch["data"]["total_count"]
        print("专区搜索成功！！！数据共%s条" % total_count )
        print(json_util.dumps(response_goodssearch["data"],ensure_ascii=False,indent=4))
    else:
        message = response_goodssearch["message"]
        print("专区搜索失败！！！原因为：%s" % message)

if __name__ == "__main__":
    goods_search("人事")