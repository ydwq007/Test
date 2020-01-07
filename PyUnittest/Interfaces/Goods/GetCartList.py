# -*- coding: utf-8 -*-
"""
接口：获取用户的购物车信息
创建人：魏奇
更新人：魏奇
更新时间：2019-08-20
"""
import Json_data,requests
from bson import json_util
import sys
sys.path.append(r"D:\IdeaProjects\seeyon\PyUnittest\TestDatas") #跨目录调用需要配置路径
import BasicDatas
import Logins.Login as Login

#获取商品基本信息地址
search_url = "%s/rest/goods/getCartList" % BasicDatas.test_url_mall



def getcartlist(user_id,Authorization):
    data = {
        "user_id" : user_id, #用户ID
        "page_index" : "1", #页数
        "page_size" : "10" #每页数量
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
        if response_search["data"]["data"]:#判断列表值是否为空
            total_count = response_search["data"]["total_count"]
            goods_id = [] #构建商品id的列表
            cart_id = [] #构建购物车id的列表
            # print(json_util.dumps(response_search["data"],ensure_ascii=False,indent=4))
            print("用户%s：获取购物车信息成功！！！数据共%s条，前10条名称分别为：" % (user_id,total_count))
            for i in response_search["data"]["data"]:
                goods_id.append(i["goods_id"])
                cart_id.append(i["cart_id"])
                print("商品id为%s   商品名称为：%s   购物车id为%s " % (i["goods_id"],i["goods_name"],i["cart_id"]))
            goods = dict(zip(goods_id,cart_id)) #构建字典
            print(goods)
            return True,total_count,goods
        else:
            print("用户%s：购物车为空！！！" % user_id)
            return True,user_id
    else:
        message = response_search["message"]
        print("用户%s：获取购物车信息失败！！！原因为：%s" % (user_id,message))
        return False

if __name__ == "__main__":
    # getcartlist()

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
    getcartlist(result_login[2],result_login[3]) #15626503750190000
