# -*- coding: utf-8 -*-
"""
接口：删除试用订单
创建人：魏奇
更新人：魏奇
更新时间：2019-10-21 15:40
描述：删除云商城试用订单数据
"""

import sys,Json_data,requests,BasicDatas
from bson import json_util
sys.path.append(r"D:\IdeaProjects\seeyon\PyUnittest\TestDatas")

def trialorderdelete(Authorization,order_id):

    #获取删除订单地址
    trialorderdelete_url = "%s/portal.php?m=mall&a=forward&mallAction=/trialOrder/delete" % BasicDatas.test_chome

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
    request_trialorderdelete = requests.post(trialorderdelete_url, data=datas,headers=header,verify=False) #调用接口（url,参数，类型）#verify=False 跳过认证

    #获取响应数据
    response_trialorderdelete= Json_data.loads(request_trialorderdelete.text)

    print("-----------打印请求数据如下：--------------")
    print(trialorderdelete_url)
    print(json_util.dumps(data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出

    #打印响应结果，以json格式输出
    print("---------打印响应结果：---------------")
    print(json_util.dumps(response_trialorderdelete,ensure_ascii=False,indent=4))
    # if "order_id" in response_trialorderdelete["data"].keys(): #通过字段判断
    if response_trialorderdelete["code"] == "1000":
        print("订单编号%s，删除成功！！！" % order_id)
        return True
    else:
        message = response_trialorderdelete["message"]
        print("订单编号%s，删除失败！！！原因为：%s" % (order_id,message))
        return False

if __name__ == "__main__":

    # Authorization = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjaG9tZSIsImlhdCI6MT" \
    #                 "U2ODYyMTc3OCwic2NvcGVzIjoicm9sZV9hY2Nlc3MiLCJleHAiOjE1NzEyMTM3NzgsInVpZCI6IjE" \
    #                 "1NjI2NTAzNzUwMTkwMDAwIn0.BsNnqAja54VzvQfsX6heEvAy7tWwe53feseUqqcogjY"
    Authorization = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjaG9tZSIsImlhdCI6MTU3MTcyMjQ4NSwic2NvcGVzIjoicm9sZV9hY2Nlc3MiLCJleHAiOjE1NzQzMTQ0ODUsInVpZCI6IjE1NjI2NTAzNzUwMTkwMDAwIn0.tx32jEsMPc8154Bm-QU4zz_iPQWOkrO7ofD9clAbl3Q"
    orderid = "15688718360390000"
    trialorderdelete(Authorization,orderid)


