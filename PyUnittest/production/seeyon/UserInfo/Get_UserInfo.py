# -*- coding: utf-8 -*-
"""
接口：获取用户信息
创建人：魏奇
更新人：魏奇
更新时间：2019-09-16
描述：chome获取用户信息（包括用户信息，所属客户单位信息，经销商信息），需要用户登录为前提
"""
import json,requests
from bson import json_util
import sys
sys.path.append("../../TestDatas") #跨目录调用需要配置路径
import BasicDatas

#获取用户信息URL
userinfo_url = "%s/portal.php" % BasicDatas.test_url_chome

def userinfo(Authorization):

    data = {
            "m":"usercenter",
            "a":"accountSetting"
        }

    #请求头
    header = {
        "Content-Type": "application/json",
        "Connection":"keep-alive",
        "Authorization":Authorization

    }

    #将请求转换为json格式
    datas = json.dumps(data)

    #调用接口（url,参数，类型）#verify=False 跳过认证
    request_userinfo = requests.post(userinfo_url, data=datas,headers=header,verify=False)

    #获取响应数据
    response_userinfo= json.loads(request_userinfo.text)

    print("-----------打印请求数据如下：--------------")
    print(userinfo_url)
    print(json_util.dumps(data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出

    #打印响应结果，以json格式输出
    print("---------打印响应结果：---------------")
    print(json_util.dumps(response_userinfo,ensure_ascii=False,indent=4))
    if "uid" in response_userinfo["data"].keys(): #通过字段判断
    # if response_userinfo["code"] == "1000":
    #     print(json_util.dumps(response_userinfo["data"],ensure_ascii=False,indent=4))
        print("-------客户单位信息为-------")
        print(json_util.dumps(response_userinfo["data"]["orgList"],ensure_ascii=False,indent=4))
        print("-------经销商信息为-------")
        print(json_util.dumps(response_userinfo["data"]["org_service"],ensure_ascii=False,indent=4))
        print("-------产品信息为-------")
        print(json_util.dumps(response_userinfo["data"]["orgProduct"],ensure_ascii=False,indent=4))
        print("获取用户信息成功！！！")
        return True
    else:
        print("获取用户信息失败！！！")
        return False

if __name__ == "__main__":
    userinfo("Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjaG9tZSIsImlhdCI6MT"
             "U2ODYyMTc3OCwic2NvcGVzIjoicm9sZV9hY2Nlc3MiLCJleHAiOjE1NzEyMTM3NzgsInVpZCI6IjE"
             "1NjI2NTAzNzUwMTkwMDAwIn0.BsNnqAja54VzvQfsX6heEvAy7tWwe53feseUqqcogjY")
    # userinfo()