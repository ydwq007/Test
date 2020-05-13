# -*- coding: utf-8 -*-
"""
接口：构造接口测试需要的各种数据
创建人：魏奇
更新人：魏奇
更新时间：2020-02-13 15:56
描述：
"""

import requests,json,re,sys
sys.path.append("../../TestDatas")
import config

# 登录获取token(针对前台账号)，并且生成前台header
def get_token(loginurl,Nomal_login_data,headers):

    login_url = "%s/portal.php" % loginurl
    datas = json.dumps(Nomal_login_data)
    Nomal_login_request = requests.post(url=login_url,data=datas,headers=headers,verify=False)
    Nomal_login_result= json.loads(Nomal_login_request.text)
    # print(Nomal_login_result)
    Nomal_login_token = Nomal_login_result["data"]["token"]["access_token"]

    # 一般header头
    new_header1 = {
                "Content-Type": "application/json",
                "Authorization":"Bearer %s" % Nomal_login_token
            }
    mdvalue1 = json.dumps(new_header1) #转为字符串
    # print("登录云商城前台后生成的一般header为：\n%s\n" % new_header1)

    # ajax header头
    new_header2 = {
        "Content-Type": "application/json",
        "X-Requested-With":"XMLHttpRequest",
        "Authorization":"Bearer %s" % Nomal_login_token
    }
    mdvalue2 = json.dumps(new_header2) #转为字符串
    # print("登录云商城前台后生成的ajax新header为：\n%s\n" % new_header2)

    return Nomal_login_token,new_header1,mdvalue1,new_header2,mdvalue2


# 登录获取MALL_ID，针对后台账号，并且生成后台header
def get_mallid(loginurl,mallurl,shop_login_data,headers):

    # 登录云商城前台
    login_url = "%s/portal.php" % loginurl
    datas = json.dumps(shop_login_data)
    shop_login_request = requests.post(url=login_url,data=datas,headers=headers,verify=False)
    shop_login_result= json.loads(shop_login_request.text)
    shop_login_token = shop_login_result["data"]["token"]["access_token"]
    new_header = {
        "Content-Type": "application/json",
        "Authorization":"Bearer %s" % shop_login_token
    }

    #切换到商家后台，获取mall_id
    cmall_url = "%s/admin" % mallurl
    # print(cmall_url)
    shop_mall_request = requests.get(url=cmall_url,headers=new_header,verify=False)
    mall_header = json.dumps(dict(shop_mall_request.headers))
    # print(mall_header)
    get_mallid = r"MALL_ID=(.*?); path" # 需要获取的对象
    mallid =  re.findall(get_mallid, mall_header) #\u4e00-\u9fa5匹配汉字，A-Z匹配大写英文
    # print(mallid)
    #更新数据
    new_mall_header = {
        "Content-Type": "application/json",
        "X-Requested-With":"XMLHttpRequest",
        "Cookie":"MALL_ID=%s" % mallid[0]
    }
    mdvalue = json.dumps(new_mall_header) #转为字符串
    # print("登录云商城后台后生成的新header为：\n%s\n" % new_mall_header)
    return shop_login_token,new_mall_header,mdvalue

# 创建普通订单
def nomal_create(loginurl,Nomal_login_data,headers,mallurl,nomal_order):

    newheader = get_token(loginurl,Nomal_login_data,headers)
    nomal_order_url = "%s/rest/order/createOrder" % mallurl
    nomal_order_data = json.dumps(nomal_order)
    nomal_order_request = requests.post(url=nomal_order_url,data=nomal_order_data,headers=newheader[1],verify=False)
    nomal_order_response = json.loads(nomal_order_request.text)
    print(nomal_order_response)
    nomal_order_id = nomal_order_response["data"]["data"]["order_id"]
    order_id = {
        "order_id":"%s" % nomal_order_id
    }
    mdvalue = json.dumps(order_id) #转为字符串
    print("订单创建成功。单号为：%s\n" % nomal_order_id)
    return nomal_order_id,order_id,mdvalue

# 商务登录
def chome_login(chomeurl,chome_login_data,headers):

    chome_url = "%s/portal.php" % chomeurl
    datas = json.dumps(chome_login_data)
    chome_login_request = requests.post(url=chome_url,data=datas,headers=headers,verify=False)
    chome_login_result= json.loads(chome_login_request.text)
    chome_login_token = chome_login_result["data"]["token"]["access_token"]
    print(chome_login_token)
    new_chome_header = {
        "Content-Type": "application/json",
        "Authorization":"Bearer %s" % chome_login_token
    }
    print(new_chome_header)
    mdvalue = json.dumps(new_chome_header) #转为字符串
    print("登录chome后生成的新header为：\n%s\n" % new_chome_header)
    return chome_login_token,new_chome_header,mdvalue

if __name__ == "__main__":

    loginurl = config.test_url_chome
    mallurl = config.test_url_mall
    Nomal_login_data = config.aloneA
    shop_login_data = config.dealer
    headers = config.headers
    nomal_order = config.nomal_order

    # test1 = get_token(loginurl,Nomal_login_data,headers)
    # test2 = get_mallid(loginurl,mallurl,shop_login_data,headers)
    test3 = nomal_create(loginurl,Nomal_login_data,headers,mallurl,nomal_order)