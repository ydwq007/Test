# -*- coding: utf-8 -*-
"""
接口：解析商品包
创建人：魏奇
更新人：魏奇
更新时间：2019-10-29 14:46
描述：
"""

# -*- coding: utf-8 -*-
"""
接口：商家后台新增商品
创建人：魏奇
更新人：魏奇
更新时间：2019-10-29 11:21
描述：创建新商品数据
"""

import sys,Json_data,requests,BasicDatas
from bson import json_util
sys.path.append(r"D:\IdeaProjects\seeyon\PyUnittest\TestDatas")

def checkGoodsPackageAnalysis(Authorization,goods_file):

    #新建商品的URL
    checkGoodsPackageAnalysis_url = "%s/admin/goods/checkGoodsPackageAnalysis" % BasicDatas.test_url_mall

    data = {
        "goods_file": goods_file
    }

    header = {
        "Content-Type": "application/json",
        "Connection":"keep-alive",
        "Authorization":Authorization
        # "MALL_ID":Authorization
    }

    datas = Json_data.dumps(data)

    #调用接口
    checkGoodsPackageAnalysis_request = requests.post(checkGoodsPackageAnalysis_url,data=datas,headers=header,verify=False)

    #打印请求数据
    print("-----------------请求数据如下：----------------------")
    print("请求地址：\n%s" % checkGoodsPackageAnalysis_url)
    print("请求数据：\n%s" % json_util.dumps(datas,ensure_ascii=False,indent=4))

    #获取响应数据
    checkGoodsPackageAnalysis_response = Json_data.loads(checkGoodsPackageAnalysis_request.text)

    #打印响应数据
    print("--------------------响应数据如下：---------------------------------")
    print(json_util.dumps(checkGoodsPackageAnalysis_response,ensure_ascii=False,indent=4))

    #判断新增成功还是失败
    if checkGoodsPackageAnalysis_response["code"] == 1000:
        goods_id =  checkGoodsPackageAnalysis_response["data"]
        print("商品新增成功！商品id为%s" %  goods_id)
    else:
        message =  checkGoodsPackageAnalysis_response["message"]
        print("商品新增失败！原因为%s" % message)

if __name__ == "__main__":
    Authorization = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjaG9tZSIsImlhdCI6MTU3MjMxMzY4Mywic2NvcGVzIjoicm9sZV9hY2Nlc3MiLCJleHAiOjE1NzQ5MDU2ODMsInVpZCI6IjE1NjI2NTAzNzUwMTkwMDAwIn0.sQw8OOIALchV6-424ggF3CYriA8p0QW6KRpe_3NkJc8"
    MALL_ID = "e20i4v6dstja9dk6pgskkbvns7"
    goods_file = "商品升级包_1572240150641170000.syz"
    checkGoodsPackageAnalysis(Authorization,goods_file)
