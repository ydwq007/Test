# -*- coding: utf-8 -*-
"""
接口：订单详情
创建人：魏奇
更新人：魏奇
更新时间：2019/9/18
描述：查询订单详情，需要登录，可以查询任意普通订单和试用单（包括属于当前人或不属于的）
"""

import sys,Json_data,requests,BasicDatas
from bson import json_util
sys.path.append(r"D:\IdeaProjects\seeyon\PyUnittest\TestDatas")

def orderdetail(Authorization,order_id):

    #获取订单详情地址
    orderdetail_url = "%s/rest/order/orderDetail" % BasicDatas.test_mall

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
    request_orderdetail = requests.post(orderdetail_url, data=datas,headers=header,verify=False) #调用接口（url,参数，类型）#verify=False 跳过认证

    #获取响应数据
    response_orderdetail= Json_data.loads(request_orderdetail.text)

    print("-----------打印请求数据如下：--------------")
    print(orderdetail_url)
    print(json_util.dumps(data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出

    #打印响应结果，以json格式输出
    print("---------打印响应结果：---------------")
    # print(json_util.dumps(response_orderdetail,ensure_ascii=False,indent=4))
    # if "order_id" in response_orderdetail["data"].keys(): #通过字段判断
    if response_orderdetail["code"] == "1000":
        if "order_id" in response_orderdetail["data"].keys():
            print(json_util.dumps(response_orderdetail["data"],ensure_ascii=False,indent=4))
            print("订单编号%s，查询成功！！！" % order_id)
        else:
            print("订单编号%s，未匹配到数据！！！" % order_id)
        return True,order_id
    else:
        message = response_orderdetail["message"]
        print("订单编号%s，查询失败！！！原因为：%s" % (order_id,message))
        return False,order_id

if __name__ == "__main__":
    Authorization = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjaG9tZSIsImlhdCI6MTU3MTY0MDQ3MSwic2NvcGVzIjoicm9sZV9hY2Nlc3MiLCJleHAiOjE1NzQyMzI0NzEsInVpZCI6IjE1NjI2NTAzNzUwMTkwMDAwIn0._UiD4ymJ2AY1S5N65tWA9S_e0Dh_V94VuH7EoM-QEqs"
    orderid = 15717082810160000
    orderdetail(Authorization,orderid)

