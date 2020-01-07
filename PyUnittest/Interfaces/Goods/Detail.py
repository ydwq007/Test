# -*- coding: utf-8 -*-
"""
接口：获取商品详情描述信息
创建人：魏奇
更新人：魏奇
更新时间：2019-08-20
"""
import json,requests
from bson import json_util
import sys
sys.path.append("../../TestDatas") #跨目录调用需要配置路径
import BasicDatas

#获取商品基本信息地址
search_url = "%s/rest/goods/detail" % BasicDatas.test_url_mall

def detail(goods_id):
    data = {
        "goods_id":goods_id #商品id
    }
    datas = json.dumps(data)
    #调用接口
    request_baseinfor = requests.post(search_url, data=datas, headers=BasicDatas.headers, verify=False) #调用接口（url,参数，类型）#verify=False 跳过认证

    #获取响应数据
    response_search= json.loads(request_baseinfor.text)

    # print("-----------打印请求数据如下：--------------")
    print(search_url)
    # print(goods_data)
    print(json_util.dumps(data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出

    #打印响应结果，以json格式输出
    print("---------打印响应结果：---------------")
    # print(json_util.dumps(response_search,ensure_ascii=False,indent=4))
    if response_search["code"] == "1000":
        if response_search["data"] is None:
            print("%s：商品详情描述信息为空！！！" % goods_id)
        else:
            print(json_util.dumps(response_search["data"],ensure_ascii=False,indent=4))
            print("%s：商品详情描述信息获取成功！！！" % goods_id)
    else:
        message = response_search["message"]
        print("%s：商品详情描述信息获取失败！！！原因为：%s" % (goods_id,message))

if __name__ == "__main__":
    detail("15657459060390000") #有详细描述15657459060390000