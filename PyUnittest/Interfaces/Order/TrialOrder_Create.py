# -*- coding: utf-8 -*-
"""
接口：订单创建
创建人：魏奇
更新人：魏奇
更新时间：2019-09-1
描述：云商城试用订单创建
"""
import Json_data,requests
from bson import json_util
import sys
sys.path.append(r"D:\IdeaProjects\seeyon\PyUnittest\TestDatas") #跨目录调用需要配置路径
import BasicDatas

#获取创建订单地址
trialordercreate_url = "%s/trialOrder/create" % BasicDatas.test_url_mall

def trialordercreate(Authorization,data):

    # data = {
    # "goods_id":"15686283260390000", #商品id，必填
    # "goods_sku_list":"617:1", #商品id列表，格式商品:商品数量，必填
    # "buyer_org_id":"-8546396329167731132", #客户单位id，必填
    # "agency_org_id":"-2763071546069595220", #服务商id，必填
    # "company_name":"16测试环境中山朗", #客户单位名称，必填
    # "order_tag":"", #订单类型，buy_now普通订单
    # "coupon_id":"", #优惠id，默认0无优惠
    # "memo":"接口测试数据" #备注
    # }

    header = {
        "Content-Type": "application/json",
        "Connection":"keep-alive",
        "Authorization":Authorization
    }
    datas = Json_data.dumps(data)
    #调用接口
    request_trialordercreate = requests.post(trialordercreate_url, data=datas,headers=header,verify=False) #调用接口（url,参数，类型）#verify=False 跳过认证

    #获取响应数据
    response_trialordercreate= Json_data.loads(request_trialordercreate.text)

    print("-----------打印请求数据如下：--------------")
    print(trialordercreate_url)
    print(json_util.dumps(data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出

    #打印响应结果，以json格式输出
    print("---------打印响应结果：---------------")
    print(json_util.dumps(response_trialordercreate,ensure_ascii=False,indent=4))
    # if "order_id" in response_trialordercreate["data"].keys(): #通过字段判断
    if response_trialordercreate["code"] == "1000":
        # print(json_util.dumps(response_trialordercreate["data"],ensure_ascii=False,indent=4))
        orderid = response_trialordercreate["data"]["order_id"]
        print("订单创建成功！！！订单号为%s" % orderid)
        return True
    else:
        message = response_trialordercreate["message"]
        print("订单创建失败！！！原因为：%s" % message)
        return False

if __name__ == "__main__":
    data = {
        "goods_id":"15686283260390000", #商品id，必填
        "goods_sku_list":"617:1", #商品id列表，格式商品:商品数量，必填
        "buyer_org_id":"-8546396329167731132", #客户单位id，必填
        "agency_org_id":"-2763071546069595220", #服务商id，必填
        "company_name":"16测试环境中山朗", #客户单位名称，必填
        "order_tag":"", #订单类型，buy_now普通订单
        "coupon_id":"", #优惠id，默认0无优惠
        "memo":"接口测试数据" #备注
    }
    Authorization = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjaG9tZSIsImlhdCI6MTU3MjMxMzY4Mywic2NvcGVzIjoicm9sZV9hY2Nlc3MiLCJleHAiOjE1NzQ5MDU2ODMsInVpZCI6IjE1NjI2NTAzNzUwMTkwMDAwIn0.sQw8OOIALchV6-424ggF3CYriA8p0QW6KRpe_3NkJc8"

    trialordercreate(Authorization,data)

    # trialordercreate()



