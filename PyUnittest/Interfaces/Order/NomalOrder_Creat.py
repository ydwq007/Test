# -*- coding: utf-8 -*-
"""
接口：订单创建 -- /order/ordercreate
创建人：魏奇
更新人：魏奇
更新时间：2019-09-18
描述：云商城普通订单创建
"""
import Json_data,requests
from bson import json_util
import sys
sys.path.append(r"D:\IdeaProjects\seeyon\PyUnittest\TestDatas") #跨目录调用需要配置路径
import BasicDatas

#获取创建订单地址
nomalordercreate_url = "%s/order/ordercreate" % BasicDatas.test_url_mall

def nomalordercreate(Authorization,data):

    # data = {
    # "goods_sku_list":"618:1", #商品id列表，格式商品:商品数量，必填
    # "buyer_org_id":"-8546396329167731132", #客户单位id，必填
    # "service_org_id":"-2763071546069595220", #服务商id，必填
    # "memo":"接口测试数据", #备注
    # "company_name":"16测试环境中山朗", #客户单位名称，必填
    # "contact_name":"测试账号1Qa!", #联系人，必填
    # "contact_phone":"15982280808", #联系电话，必填
    # "order_tag":"buy_now", #订单类型，buy_now普通订单
    # "coupon_id":"0" #优惠id，默认0无优惠
    # }

    header = {
        "Content-Type": "application/json",
        "Connection":"keep-alive",
        "Authorization":Authorization
    }
    datas = Json_data.dumps(data)
    #调用接口
    request_nomalordercreate = requests.post(nomalordercreate_url, data=datas,headers=header,verify=False) #调用接口（url,参数，类型）#verify=False 跳过认证

    #获取响应数据
    response_nomalordercreate= Json_data.loads(request_nomalordercreate.text)

    print("-----------打印请求数据如下：--------------")
    print(nomalordercreate_url)
    print(json_util.dumps(data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出

    #打印响应结果，以json格式输出
    print("---------打印响应结果：---------------")
    print(json_util.dumps(response_nomalordercreate,ensure_ascii=False,indent=4))
    # if "order_id" in response_nomalordercreate["data"].keys(): #通过字段判断
    if response_nomalordercreate["code"] == 0:
    #     print(json_util.dumps(response_nomalordercreate["data"],ensure_ascii=False,indent=4))
        orderid = response_nomalordercreate["data"]["order_id"]
        print("订单创建成功！！！订单号为%s" % orderid)
        return True,orderid
    else:
        message = response_nomalordercreate["message"]
        print("订单创建失败！！！原因为：%s" % message)
        return False

if __name__ == "__main__":
    data = {
        "goods_sku_list":"618:1", #商品id列表，格式商品:商品数量
        "buyer_org_id":"-8546396329167731132", #客户单位id,
        "service_org_id":"-2763071546069595220", #服务商id
        "memo":"接口测试数据", #备注
        "company_name":"16测试环境中山朗", #客户单位名称
        "contact_name":"测试账号1Qa!", #联系人
        "contact_phone":"15982280808", #联系电话
        "order_tag":"buy_now", #订单类型，buy_now普通订单
        "coupon_id":"0" #优惠id，默认0无优惠
    }

    data1 = {
        "goods_sku_list":"1479:1", #商品id列表，格式商品:商品数量
        "buyer_org_id":"4015675806454401654", #客户单位id,
        "service_org_id":"-2763071546069595220", #服务商id
        "memo":"接口测试数据", #备注
        "company_name":"70测试环境_crm", #客户单位名称
        "contact_name":"测试账号1Qa!", #联系人
        "contact_phone":"15982280808", #联系电话
        "order_tag":"buy_now", #订单类型，buy_now普通订单
        "coupon_id":"0" #优惠id，默认0无优惠
    }

    Authorization = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjaG9tZSIsImlhdCI6MTU3MTY0MDQ3MSwic2NvcGVzIjoicm9sZV9hY2Nlc3MiLCJleHAiOjE1NzQyMzI0NzEsInVpZCI6IjE1NjI2NTAzNzUwMTkwMDAwIn0._UiD4ymJ2AY1S5N65tWA9S_e0Dh_V94VuH7EoM-QEqs"
    nomalordercreate(Authorization,data1)




