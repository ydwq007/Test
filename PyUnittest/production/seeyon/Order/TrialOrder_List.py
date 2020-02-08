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
trialorderlist_url = "%s/portal.php?m=mall&a=forward&mallAction=/trialOrder/list" % BasicDatas.test_url_chome

def trialorderlist(Authorization,data):

    # data = {
    #     "page":"1", #页数，必填
    #     "list_rows":"100", #每页数量，必填
    #     "start_time":"2019-05-04", #开始时间，必填
    #     "end_time":"2019-09-04", #结束时间，必填
    #     "keyword":"" #关键字
    # }

    header = {
        "Content-Type": "application/json",
        "Connection":"keep-alive",
        "Authorization":Authorization
    }
    datas = json.dumps(data)
    #调用接口
    request_trialorderlist = requests.post(trialorderlist_url, data=datas,headers=header,verify=False) #调用接口（url,参数，类型）#verify=False 跳过认证

    #获取响应数据
    response_trialorderlist= json.loads(request_trialorderlist.text)

    print("-----------打印请求数据如下：--------------")
    print(trialorderlist_url)
    print(json_util.dumps(data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出

    #打印响应结果，以json格式输出
    print("---------打印响应结果：---------------")
    print(json_util.dumps(response_trialorderlist,ensure_ascii=False,indent=4))
    # if "order_id" in response_trialorderlist["data"].keys(): #通过字段判断
    if response_trialorderlist["code"] == "1000":
        count = response_trialorderlist["data"]["total"]
        if count != 0:
            orderid = []
            for i in response_trialorderlist["data"]["data"]:
                orderid.append(i["order_id"])
            print("查询成功，符合条件的试用单总共查询出%s条数据！！！\n"
                  "订单号为%s" % (count,orderid))
            return True
        else:
            print("查询成功，无符合条件的试用单数据")
            return True
    else:
        message = response_trialorderlist["message"]
        print("试用单查询失败！！！原因为：%s" % message)
        return False

if __name__ == "__main__":
    data = {
        "page":"1", #页数，必填
        "list_rows":"100", #每页数量，必填
        "start_time":"2019-05-04", #开始时间，必填
        "end_time":"2019-09-04", #结束时间，必填
        "keyword":"" #关键字
    }
    trialorderlist("Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjaG9tZSIsImlhdCI6MT"
                     "U2ODYyMTc3OCwic2NvcGVzIjoicm9sZV9hY2Nlc3MiLCJleHAiOjE1NzEyMTM3NzgsInVpZCI6IjE"
                     "1NjI2NTAzNzUwMTkwMDAwIn0.BsNnqAja54VzvQfsX6heEvAy7tWwe53feseUqqcogjY",data)

    # trialorderlist()