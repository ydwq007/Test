# -*- coding: utf-8 -*-
"""
接口：封装商品搜索接口 - 移动端
创建人：魏奇
更新人：魏奇
更新时间：2019-08-20
说明：
"""

import requests,json
from bson import json_util
# logging.basicConfig(level=logging.DEBUG)
import sys
sys.path.append("../../TestDatas") #跨目录调用需要配置路径
import BasicDatas

#商品搜索接口地址
search_url = "%s/rest/search/searchGoods" % BasicDatas.test_url_mall

def goods_search(keywords):
    data = {

            "keywords":keywords, #搜索关键字
            "scene":"all",     #搜索场景，all：所有；free：免费商品
            "sale":"0",        #销量排序，0：不按销量，1：销量排行（sale、up_time_sort和price_sort 三者选其一，其余值清空）
            "up_time_sort":"", #上架顺序，desc / asc
            "price_sort":"asc",#价格排序，desc / asc
            "category_id":"",  #分类ID，允许多个值，英文逗号分隔
            "group_ids":"",  #标签ID，允许多个值，英文逗号分隔
            "terminal":"",   #适配终端，1全选 2pc端 3移动端
            "experience_centre":"" #体验中心，0不是；1是

    }
    datas = json.dumps(data)
    #调用接口
    request_search = requests.post(search_url, data=datas, headers=BasicDatas.headers, verify=False) #调用接口（url,参数，类型）#verify=False 跳过认证

    #获取响应数据
    response_search= json.loads(request_search.text)

    # print("-----------打印请求数据如下：--------------")
    print(search_url)
    print(data)
    # print(json_util.dumps(data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出

    #打印响应结果，以json格式输出
    print("---------打印响应结果：---------------")
    # print(json_util.dumps(response_search,ensure_ascii=False,indent=4))
    if response_search["code"] == "1000":
        if response_search["data"]["data"]:#判断列表值是否为空
            total_count = response_search["data"]["total_count"]
            print(json_util.dumps(response_search["data"],ensure_ascii=False,indent=4))
            print("关键字%s：商品搜索成功！！！数据共%s条，前10条数据名称分别为：" % (keywords,total_count ))
            for i in response_search["data"]["data"]:
                print(i["goods_name"])
            goods_id = response_search["data"]["data"][0]["goods_id"]
            return True,goods_id
        else:
            print("%s：商品信息为空！！！" % keywords )
            return True
    else:
        message = response_search["message"]
        print("关键字%s：商品搜索失败！！！原因为：%s" % (keywords,message))
        return False

if __name__ == "__main__":
    goods_search()