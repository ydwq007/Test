# -*- coding: utf-8 -*-
"""
接口：定制单提交或修改
创建人：魏奇
更新人：魏奇
更新时间：2019/9/18 16:26
描述：接口需要修改，暂缓封装
"""

import sys,Json_data,requests,BasicDatas
from bson import json_util
sys.path.append(r"D:\IdeaProjects\seeyon\PyUnittest\TestDatas")

def customizeorder(Authorization,type=1,order_id=""):

    #获取订单详情地址
    customizeorder_url = "%s/rest/order/submitCustomizeOrder" % BasicDatas.test_mall

    if type == 1:#新增定制单参数
        data = {
            "order_name": "定制单名称", #定制单名称
            "customize_type": "3", #定制单类型
            "customize_info": "", #定制单详情
            "customize_goods_id": "", #定制的商品ID
            "require_file_name": "", #需求文档名称
            "require_file_url": "", #需求文档地址
            "customize_case_id": "2",  #案例id
            "industry":"行业",          #行业
            "buyer_org_name":"单位名称",
        }
    else:#修改定制单参数
        data = {
            "order_name": "定制单名称", #定制单名称
            "customize_type": "3", #定制单类型
            "customize_info": "", #定制单详情
            "customize_goods_id": "", #定制的商品ID
            "require_file_name": "", #需求文档名称
            "require_file_url": "", #需求文档地址
            "customize_case_id": "2",  #案例id
            "industry":"行业",          #行业
            "buyer_org_name":"单位名称",
            "order_id":order_id        #修改时候需要
        }

    header = {
        "Content-Type": "application/json",
        "Connection":"keep-alive",
        "Authorization":Authorization
    }

    datas = Json_data.dumps(data)
    #调用接口
    request_customizeorder = requests.post(customizeorder_url, data=datas,headers=header,verify=False) #调用接口（url,参数，类型）#verify=False 跳过认证

    #获取响应数据
    response_customizeorder= Json_data.loads(request_customizeorder.text)

    print("-----------打印请求数据如下：--------------")
    print(customizeorder_url)
    print(json_util.dumps(data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出

    #打印响应结果，以json格式输出
    print("---------打印响应结果：---------------")
    print(json_util.dumps(response_customizeorder,ensure_ascii=False,indent=4))
    # if "order_id" in response_customizeorder["data"].keys(): #通过字段判断
    if response_customizeorder["code"] == "1000":
        print(json_util.dumps(response_customizeorder["data"],ensure_ascii=False,indent=4))
        print("定制单提交成功，定制单编号为%s！！！" % order_id)
        return True
    else:
        message = response_customizeorder["message"]
        print("定制单提交失败！！！原因为：%s" % message)
        return False

if __name__ == "__main__":
    customizeorder("Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjaG9tZSIsImlhdCI6MT"
                          "U2ODYyMTc3OCwic2NvcGVzIjoicm9sZV9hY2Nlc3MiLCJleHAiOjE1NzEyMTM3NzgsInVpZCI6IjE"
                          "1NjI2NTAzNzUwMTkwMDAwIn0.BsNnqAja54VzvQfsX6heEvAy7tWwe53feseUqqcogjY")

    # customizeorder()