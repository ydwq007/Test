# -*- coding: utf-8 -*-
"""
接口：删除普通订单
创建人：魏奇
更新人：魏奇
更新时间：2019-10-21 15:59
描述：云商城普通订单的删除操作（未完成）
"""

import sys,Json_data,requests,BasicDatas
from bson import json_util
sys.path.append(r"D:\IdeaProjects\seeyon\PyUnittest\TestDatas")

def nomalorderdelete(Authorization,order_id):

    #获取删除订单地址
    nomalorderdelete_url = "%s/order/deleteOrder" % BasicDatas.test_mall

    data = {
        "order_id":order_id #订单编号
    }

    header = {
        "Content-Type": "application/json",
        "Connection":"keep-alive",
        "Authorization":Authorization
    }

    datas = Json_data.dumps(data)
    #调用接口
    request_nomalorderdelete = requests.post(nomalorderdelete_url, data=datas,headers=header,verify=False) #调用接口（url,参数，类型）#verify=False 跳过认证

    print(request_nomalorderdelete.text)
    print(type(request_nomalorderdelete.text))

    #获取响应数据
    response_nomalorderdelete= Json_data.loads(request_nomalorderdelete.text)
    # response_nomalorderdelete= json.load(request_nomalorderdelete.text)

    print("-----------打印请求数据如下：--------------")
    print(nomalorderdelete_url)
    print(json_util.dumps(data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出

    #打印响应结果，以json格式输出
    print("---------打印响应结果：---------------")

    print(json_util.dumps(response_nomalorderdelete,ensure_ascii=False,indent=4))
    # if "order_id" in response_nomalorderdelete["data"].keys(): #通过字段判断
    if response_nomalorderdelete["code"] == "0":
        print("订单编号%s，删除成功！！！" % order_id)
        return True,order_id
    else:
        message = response_nomalorderdelete["message"]
        print("订单编号%s，删除失败！！！原因为：%s" % (order_id,message))
        return False,order_id

if __name__ == "__main__":
    Authorization = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjaG9tZSIsImlhdCI6MTU3MjMxMzY4Mywic2NvcGVzIjoicm9sZV9hY2Nlc3MiLCJleHAiOjE1NzQ5MDU2ODMsInVpZCI6IjE1NjI2NTAzNzUwMTkwMDAwIn0.sQw8OOIALchV6-424ggF3CYriA8p0QW6KRpe_3NkJc8"
    orderid = 15723146540160000
    mallid = "e20i4v6dstja9dk6pgskkbvns7"
    nomalorderdelete(mallid,orderid)