# -*- coding: utf-8 -*-
"""
接口：封装标签搜索接口 - 移动端
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
search_url = "%s/rest/search/searchGroupTag" % BasicDatas.test_url_mall

def grouptag_search(keywords):
    data = {
        "tag_type":keywords, #标签类型，默认为4（1：服务商 2：专家 3：案例 4：商品，0：通用）
        "category_level":"1" #分类层级，默认为2（1-5 共5级）
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
        account = len(response_search["data"]["group_tag_list"])
        print(json_util.dumps(response_search["data"],ensure_ascii=False,indent=4))
        print("类型为%s：标签搜索成功！！！共%s条数据，数据分别为：" % (keywords,account ))
        for i in response_search["data"]["group_tag_list"]:
            print(i["group_name"])
    else:
        message = response_search["message"]
        print("类型为%s：标签搜索失败！！！原因为：%s" % (keywords,message))

if __name__ == "__main__":
    grouptag_search("4")