# -*- coding: utf-8 -*-
"""
接口：封装服务商搜索接口 - 移动端
创建人：魏奇
更新人：魏奇
更新时间：2019-08-20
说明：
"""

import requests,json
from bson import json_util
# logging.basicConfig(level=logging.DEBUG)
import sys
sys.path.append("../../TestDatas") #跨目录调用需要配置路径
import BasicDatas


#案例搜索接口地址
search_url = "%s/rest/search/searchProvider" % BasicDatas.test_url_mall

def provider_search(keywords):
    data = {
        "keywords":keywords, #搜索关键字
        "shop_credit":"", #店铺信用，desc / asc  （shop_credit和create_time二选一，其余清空）
        "create_time":"asc"#创建时间，desc / asc
    }
    datas = json.dumps(data)
    #调用接口
    request_search = requests.post(search_url, data=datas, headers=BasicDatas.headers, verify=False) #调用接口（url,参数，类型）#verify=False 跳过认证

    #获取响应数据
    response_search= json.loads(request_search.text)

    # print("-----------打印请求数据如下：--------------")
    print(search_url)
    print(data)
    # print(json_util.dumps(data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出

    #打印响应结果，以json格式输出
    print("---------打印响应结果：---------------")
    # print(json_util.dumps(response_search,ensure_ascii=False,indent=4))
    if response_search["code"] == "1000":
        if response_search["data"]["data"]:#判断列表值是否为空
            total_count = response_search["data"]["total_count"]
            print(json_util.dumps(response_search["data"],ensure_ascii=False,indent=4))
            print("关键字%s：店铺搜索成功！！！数据共%s条，前10条数据名称分别为：" % (keywords,total_count ))
            for i in response_search["data"]["data"]:
                print(i["shop_name"])
        else:
            print("%s：店铺信息为空！！！" % keywords )
    else:
        message = response_search["message"]
        print("关键字%s：店铺搜索失败！！！原因为：%s" % (keywords,message))

if __name__ == "__main__":
    provider_search("店铺1111")