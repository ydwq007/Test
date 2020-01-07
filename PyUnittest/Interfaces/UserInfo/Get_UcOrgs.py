# -*- coding: utf-8 -*-
"""
接口：获取用户基本信息
创建人：魏奇
更新人：魏奇
更新时间：2019-09-17
描述：cloud获取用户信息（包括用户信息，所属客户单位信息，经销商信息），需要用户登录为前提
"""

import json,requests
from bson import json_util
import sys
sys.path.append("../../TestDatas") #跨目录调用需要配置路径
import BasicDatas


def getServiceOrgId(Authorization):

    # __token__ = token #登录token

    #请求头
    header = {
        "Content-Type": "application/json",
        "Connection":"keep-alive",
        "Authorization":Authorization
    }

    #获取用户信息URL
    # getServiceOrgId_url = "%s/rest/order/getServiceOrgId?__token__=%s" % (BasicDatas.test_url_mall,__token__)
    getServiceOrgId_url = "%s/rest/order/getServiceOrgId" % BasicDatas.test_url_mall

    #调用接口（url,参数，类型）#verify=False 跳过认证
    request_getServiceOrgId = requests.post(getServiceOrgId_url, headers=header,verify=False)

    #获取响应数据
    response_getServiceOrgId= json.loads(request_getServiceOrgId.text)

    print("-----------打印请求数据如下：--------------")
    print(getServiceOrgId_url)

    #打印响应结果，以json格式输出
    print("---------打印响应结果：---------------")
    print(json_util.dumps(response_getServiceOrgId,ensure_ascii=False,indent=4))
    # if "uid" in response_getServiceOrgId["data"].keys(): #通过字段判断
    if response_getServiceOrgId["code"] == "1000":
        # print(json_util.dumps(response_getServiceOrgId["data"],ensure_ascii=False,indent=4))
        print("-------客户单位信息为-------")
        print(json_util.dumps(response_getServiceOrgId["data"]["orgList"],ensure_ascii=False,indent=4))
        print("-------经销商信息为-------")
        print(json_util.dumps(response_getServiceOrgId["data"]["org_service"],ensure_ascii=False,indent=4))
        print("-------产品信息为-------")
        print(json_util.dumps(response_getServiceOrgId["data"]["orgProduct"],ensure_ascii=False,indent=4))
        print("获取用户的单位成功！！！")
        return True
    else:
        ms = response_getServiceOrgId["message"]
        print("获取用户的单位失败！！！原因为：%s" % ms)
        return False

if __name__ == "__main__":
    # getServiceOrgId("Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjaG9"
    #                         "tZSIsImlhdCI6MTU2ODY4MzI4NSwic2NvcGVzIjoicm9sZV9hY2Nl"
    #                         "c3MiLCJleHAiOjE1NzEyNzUyODUsInVpZCI6IjE1NjI2NTAzNzUwMT"
    #                         "kwMDAwIn0.8SutvK4X1HMzabdxpDj7Q6FuHkzPbqLyO_DsN1r6H0c")

    getServiceOrgId()

