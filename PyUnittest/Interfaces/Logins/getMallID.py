# -*- coding: utf-8 -*-
"""
接口：获取mall_id
创建人：魏奇
更新人：魏奇
更新时间：2019-10-29 15:21
描述：
"""

import sys,Json_data,requests,BasicDatas,re
from bson import json_util
sys.path.append(r"D:\IdeaProjects\seeyon\PyUnittest\TestDatas")

def login_shop(username,password):

    #登录商家后台的URL
    login_shop_url = "%s/portal.php?m=user&a=loginSub" % BasicDatas.test_url_chome

    data = {
        "account_type":1,
        "username":username,
        "password":password
    }

    header = {
        "Content-Type": "application/json",
        "Connection":"keep-alive"
    }

    datas = Json_data.dumps(data)

    #调用接口
    login_shop_request = requests.post(login_shop_url,data=datas,headers=header,verify=False)

    #打印请求数据
    print("-----------------请求数据如下：----------------------")
    print("请求地址：\n%s" % login_shop_url)
    print("请求数据：\n%s" % json_util.dumps(datas,ensure_ascii=False,indent=4))
    print("请求头：\n%s" % login_shop_request.headers)

    #获取ucuid
    # print(type(login_shop_request.headers))
    header_1 = Json_data.loads(Json_data.dumps(dict(login_shop_request.headers)))
    # print(type(header_1))
    # print(header_1)
    #利用re正则，获取ucuid
    re_ucuid_1 = re.findall(r'ucuid=(.+?);', Json_data.dumps(header_1)) #\u4e00-\u9fa5匹配汉字，A-Z匹配大写英文
    # print(type(re_ucuid_1))
    print(re_ucuid_1)
    uc_header_1 = {
        "ucuid":re_ucuid_1[0]
    }

    #获取响应数据
    login_shop_response = Json_data.loads(login_shop_request.text)

    #打印响应数据
    print("--------------------响应数据如下：---------------------------------")
    print(json_util.dumps(login_shop_response,ensure_ascii=False,indent=4))

    #判断新增成功还是失败
    if "uid" in login_shop_response.keys(): #通过字段判断:
        uid =  login_shop_response["uid"]
        print("登录商家后台成功！uid为%s" %  uid)

        #重定向URL
        #登录跳转到商家后台
        # back_url = "https://testchome.seeyon.com/portal.php?m=user&a=loginJump&back_url=https%3A%2F%2Ftestcloud.seeyon.com%2Fadmin%2Flogin"
        # back_url_request = requests.get(back_url,headers=uc_header_1,verify=False)

        #登录跳转到商城前台
        back_url= "https://testchome.seeyon.com/portal.php?m=user&a=loginJump&back_url=https%3A%2F%2Ftestcloud.seeyon.com%2Fc%2Findex"
        seesion = requests.session()
        back_url_request = seesion.get(back_url,headers=uc_header_1,verify=False,allow_redirects=False)#allow_redirects重定向

        # back_url_request = requests.get(back_url,headers=uc_header_1,verify=False)
        back_url_response = back_url_request.text
        # print(back_url_response)



        header_2 = Json_data.loads(Json_data.dumps(dict(back_url_request.headers)))
        # print(type(header_2))
        # print(header_2)
        #利用re正则，获取back_re_url
        re_ucuid_2 = re.findall(r'ucuid=(.+?);', Json_data.dumps(header_2)) #\u4e00-\u9fa5匹配汉字，A-Z匹配大写英文
        # print(type(re_ucuid_2))
        print(re_ucuid_2)
        uc_header_2 = {
            "ucuid":re_ucuid_2[0]
        }


        #获取api/uc的URL
        #利用re正则，获取mallid_url
        re_url = re.findall(r'https://testcloud.seeyon.com/api/uc(.+?)"', back_url_response) #\u4e00-\u9fa5匹配汉字，A-Z匹配大写英文
        # print(type(re_url))
        #list转字符串
        re_str = "".join(re_url)
        mallid_url = "https://testcloud.seeyon.com/api/uc%s" % re_str
        print(mallid_url)

        #获取mallid
        getmallid_request = requests.get(mallid_url,headers=uc_header_2,verify=False)
        print("响应头：\n%s" % getmallid_request.headers)
        mallid = getmallid_request.headers["Set-Cookie"][8:34]
        # print(type(mallid))
        print("获取mallid成功！MALL_ID为%s" %  mallid)

        #跳转商家后台
        shop_admin_url = "https://testcloud.seeyon.com/admin/login"
        uc_header_3 = {
            "MALL_ID":mallid
        }
        shop_admin_request = requests.post(shop_admin_url,headers=uc_header_3,verify=False)
        print(shop_admin_request.text)
        return True,mallid
    else:
        message =  login_shop_response["message"]
        print("登录商家后台失败！原因为%s" % message)
        return False,message

if __name__ == "__main__":
    username = "gold001"
    password = "123456"
    login_shop(username,password)