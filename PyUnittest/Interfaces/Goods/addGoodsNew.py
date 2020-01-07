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
sys.path.append('../Interfaces') #跨目录调用需要配置路径,接口路径
import Logins.getMallID as Login

def addGoodsNew(MALL_ID):

    #新建商品的URL
    addGoodsNew_url = "%s/admin/goods/addGoodsNew" % BasicDatas.test_url_mall

    data = {
            "goods_id": "0",
            "goods_type": "10",
            "release_id": "0",
            "goods_name": "接口测试商品-102901",
            "introduction": "商品介绍",
            "category_id": "6",
            "group_id_array": "",
            "market_price": "0",
            "sales": "111",
            "stock": "222",
            "goods_key": "102901",
            "picture_url": "https://test-pic-2-bucket.obs.cn-north-1.myhuaweicloud.com:443/图10_1564555621103170000.jpg",
            "img_array": "https://test-pic-2-bucket.obs.cn-north-1.myhuaweicloud.com:443/图10_1564555621103170000.jpg",
            "goods_explain": "推荐说明",
            "keywords": "关键词",
            "description": "<p>商品详情<</p>",
            "img_id_array": "",
            "goods_video_address": "https://test-vd-2-bucket.obs.cn-north-1.myhuaweicloud.com:443/VID_20190326_095201_1572326916850170000.mp4",
            "adaptation_type": "1",
            "adaptation_version": "all",
            "version": "V1.2.3",
            "experience_url_pc": "https://testcmanager.seeyon.com",
            "experience_url_wap": "https://testcmanager.seeyon.com",
            "experiences": "1",
            "is_download": "1",
            "sale_range": "",
            "price_type": "3",
            "price": "1",
            "charging_mode": "1",
            "charging_frequency": "0",
            "charging_duration": "0",
            "duration_unit": "0",
            "probation_status": "1",
            "supply_range": "173",
            "case_ids": "148,149",
            "must_goods_ids": "15640464880160000,15722278320160000",
            "group_tag_ids": "141",
            "experience_type": "1",
            "shop_category": "0",
            "demo_type": "2",
            "demo_h5_address": "",
            "demo_video_address": "https://test-vd-2-bucket.obs.cn-north-1.myhuaweicloud.com:443/VID_20190326_095125_1572326772589170000.mp4",
            "sort": "0",
            "goods_app_id": "1567002213734958850",
            "designer":"设计师",
            "designer_org":"设计师单位",
            "adaptation_platform":""
        }

    header = {
        "Content-Type": "application/json",
        "Connection":"keep-alive",
        "MALL_ID":MALL_ID
    }

    datas = Json_data.dumps(data)

    #调用接口
    addGoodsNew_request = requests.post(addGoodsNew_url,data=datas,headers=header,verify=False)

    #打印请求数据
    print("-----------------请求数据如下：----------------------")
    print("请求地址：\n%s" % addGoodsNew_url)
    print("请求头：\n%s" % header)
    print("请求数据：\n%s" % json_util.dumps(datas,ensure_ascii=False,indent=4))

    #获取响应数据
    addGoodsNew_response = Json_data.loads(addGoodsNew_request.text)

    #打印响应数据
    print("--------------------响应数据如下：---------------------------------")
    print(json_util.dumps(addGoodsNew_response,ensure_ascii=False,indent=4))

    #判断新增成功还是失败
    if addGoodsNew_response["code"] == 1000:
        goods_id =  addGoodsNew_response["data"]
        print("商品新增成功！商品id为%s" %  goods_id)
    else:
        message =  addGoodsNew_response["message"]
        print("商品新增失败！原因为%s" % message)

if __name__ == "__main__":
    login = Login.login_shop("gold001","123456") #调用接口
    MALL_ID = login[1]
    shop_admin_url = "https://testcloud.seeyon.com/admin/login"
    header_shop = {
        "MALL_ID":MALL_ID
    }
    shop_admin_request = requests.post(shop_admin_url,headers=header_shop,verify=False)
    print("--------------\n %s" % MALL_ID)
    addGoodsNew(MALL_ID)
