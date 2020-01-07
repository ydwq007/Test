# -*- coding: utf-8 -*-
"""
接口：清空购物车或删除购物车商品
创建人：魏奇
更新人：魏奇
更新时间：2019-08-22
"""
import Json_data,requests
from bson import json_util
import sys
sys.path.append(r"D:\IdeaProjects\seeyon\PyUnittest\TestDatas") #跨目录调用需要配置路径
import BasicDatas
import Logins.Login as Login

#获取商品基本信息地址
search_url = "%s/rest/goods/cleanCart" % BasicDatas.test_url_mall

def cleancart(user_id,Authorization,clean=True,cart_ids=""):
    data = {
        "user_id":user_id, #用户id
        "clean": clean, #是否情况购物车，ture：清空；false 不清空表示删除
        "cart_ids": cart_ids #删除时的购物车ID
    }

    header = {
        "Content-Type": "application/json",
        "Connection":"keep-alive",
        "Authorization":Authorization
    }
    datas = Json_data.dumps(data)
    #调用接口
    request_baseinfor = requests.post(search_url, data=datas,headers=header,verify=False) #调用接口（url,参数，类型）#verify=False 跳过认证

    #获取响应数据
    response_search= Json_data.loads(request_baseinfor.text)

    # print("-----------打印请求数据如下：--------------")
    print(search_url)
    # print(goods_data)
    print(json_util.dumps(data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出

    #打印响应结果，以json格式输出
    print("---------打印响应结果：---------------")
    print(json_util.dumps(response_search,ensure_ascii=False,indent=4))
    if response_search["code"] == "1000":
        print(json_util.dumps(response_search["data"],ensure_ascii=False,indent=4))
        print("清空购物车成功！！！")
        return True
    else:
        message = response_search["message"]
        print("清空购物车失败！！！原因为：%s" % message)
        return False

if __name__ == "__main__":
    # cleancart()

    user =  "gold001" #用户名
    passw = "123456" #密码

    #登录
    try:
        result_login = Login.login_mobile(user, passw, "") #获取接口成功或失败的标记
    except TypeError:
        print("验证码次数超过最多限制,SendCode接口报错")
    except IndexError:
        print("序列中没有此索引(index),SendCode接口报错")
    finally:
        print("已调用登录接口")
    cleancart(result_login[2],result_login[3])