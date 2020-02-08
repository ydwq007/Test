# -*- coding: utf-8 -*-
"""
接口：添加购物车
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
search_url = "%s/rest/goods/addCart" % BasicDatas.test_url_mall

def addcart(user_id,goods_id,Authorization):
    data = {
        "user_id" : user_id, #用户ID
        "goods_id" : goods_id, #商品ID
        "goods_num" : "1", #商品数量
        "bl_id": "", #组合套装ID
        "must_buy_goods": "" #必购组件ID（字符串，英文逗号隔开）
    }

    header = {
        "Content-Type": "application/json",
        "Connection":"keep-alive",
        "Authorization":Authorization
    }
    datas = json.dumps(data)
    #调用接口
    request_baseinfor = requests.post(search_url, data=datas,headers=header,verify=False) #调用接口（url,参数，类型）#verify=False 跳过认证

    #获取响应数据
    response_search= json.loads(request_baseinfor.text)

    # print("-----------打印请求数据如下：--------------")
    print(search_url)
    # print(goods_data)
    print(json_util.dumps(data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出

    #打印响应结果，以json格式输出
    print("---------打印响应结果：---------------")
    print(json_util.dumps(response_search,ensure_ascii=False,indent=4))
    if response_search["code"] == "1000":
        print(json_util.dumps(response_search["data"],ensure_ascii=False,indent=4))
        print("%s：商品加入购物车成功！！！" % goods_id)
        return True
    else:
        message = response_search["message"]
        print("%s：商品加入购物车失败！！！原因为：%s" % (goods_id,message))
        return False

if __name__ == "__main__":
    addcart()
    # user =  "gold001" #用户名
    # passw = "123456" #密码
    #
    # #登录
    # try:
    #     result_login = Login.login_mobile(user,passw,"") #获取接口成功或失败的标记
    # except TypeError:
    #     print("验证码次数超过最多限制,SendCode接口报错")
    # except IndexError:
    #     print("序列中没有此索引(index),SendCode接口报错")
    # finally:
    #     print("已调用登录接口")
    # addcart(result_login[2],"15657459060390000"，result_login[3])