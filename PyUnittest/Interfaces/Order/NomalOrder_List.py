# -*- coding: utf-8 -*-
"""
接口：试用订单列表
创建人：魏奇
更新人：魏奇
更新时间：2019-09-18
描述：获取试用单列表数据
"""
import json,requests
from bson import json_util
import sys
sys.path.append("../../TestDatas") #跨目录调用需要配置路径
import BasicDatas

#获取创建订单地址
nomalorderlist_url = "%s/rest/order/orderList" % BasicDatas.test_url_mall

def nomalorderlist(Authorization,data):

    header = {
        "Content-Type": "application/json",
        "Connection":"keep-alive",
        "Authorization":Authorization
    }

    datas = json.dumps(data)
    #调用接口
    request_nomalorderlist = requests.post(nomalorderlist_url, data=datas,headers=header,verify=False) #调用接口（url,参数，类型）#verify=False 跳过认证

    #获取响应数据
    response_nomalorderlist= json.loads(request_nomalorderlist.text)

    print("-----------打印请求数据如下：--------------")
    print(nomalorderlist_url)
    print(json_util.dumps(data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出

    #打印响应结果，以json格式输出
    print("---------打印响应结果：---------------")
    print(json_util.dumps(response_nomalorderlist,ensure_ascii=False,indent=4))
    # if "order_id" in response_nomalorderlist["data"].keys(): #通过字段判断
    if "total_count" in response_nomalorderlist["data"].keys():
        count = response_nomalorderlist["data"]["total_count"]
        if count != 0:
            orderid = []
            for i in response_nomalorderlist["data"]["data"]:
                orderid.append(i["order_id"])
            print("查询成功，符合条件的普通订单总共查询出%s条数据！！！\n"
                  "订单号为%s" % (count,orderid))
        else:
            print("查询成功，无符合条件的普通订单数据")
        return True
    else:
        message = response_nomalorderlist["message"]
        print("试用单查询失败！！！原因为：%s" % message)
        return False

if __name__ == "__main__":
    data = {
        "status":"all", #订单状态，必填，0待确认，1待认证，3交易完成，4已取消，all全部
        "page_index":"1", #页数，必填
        "page_size":"100", #每页展示数量，必填
        "keywords":"" #关键字
    }
    # data = "status=all&page=1&start_time=&order_no="
    nomalorderlist("Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjaG9tZSIsImlhdCI6MT"
                          "U2ODYyMTc3OCwic2NvcGVzIjoicm9sZV9hY2Nlc3MiLCJleHAiOjE1NzEyMTM3NzgsInVpZCI6IjE"
                          "1NjI2NTAzNzUwMTkwMDAwIn0.BsNnqAja54VzvQfsX6heEvAy7tWwe53feseUqqcogjY",data)

    # nomalorderlist()
