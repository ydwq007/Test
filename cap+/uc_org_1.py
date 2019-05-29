# -*- coding: utf-8 -*-
import requests,json,logging,csv
from bson import json_util
logging.basicConfig(level=logging.DEBUG)

# class UcOrg():
    # def __init__(self,name,type,subType,shortName):
    #     self.name = name
    #     self.type = type
    #     self.subType = subType
    #     self.shortName = shortName
    #     data = {
    #         "name":self.name,
    #         "type":self.type,
    #         "subType":self.subType,
    #         "shortName":self.shortName,
    #         "code":"1",
    #         "filesNo":"0",
    #         "address":"成都市",
    #         "isBuyed":"0",
    #         "ylAccount":"1",
    #         "industry":"测试数据",
    #         "status":"1"
    #     }
    #
    #     datas = json.dumps(data)
    #     print(datas)
    #
    # def uc(self):
    # def __init__(self,uc_org_url,datas,headers):
    #     count = 0
    #     for u in self.datas:
    #         count += 1
    #
    #         r = requests.post(uc_org_url, data=datas, headers=headers) #调用接口（url,参数，类型）
    #         re= json.loads(r.text) #获取响应数据
    #         success = []
    #         fail = []
    #         account1 = len(success)
    #         account2 = len(fail)
    #
    #         print("-----------打印请求数据如下：--------------")
    #         print(json_util.dumps(data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出
    #
    #         print("---------打印同步数据结果：---------------")
    #         print(json_util.dumps(re,ensure_ascii=False,indent=4)) #打印响应结果，以json格式输出
    #         print(r.json) #打印响应状态码
    #         if r.status_code == 200:
    #             print("同步数据成功！！！")
    #             success.append(u)
    #         else:
    #             print("同步数据失败！！！")
    #             fail.append(u)
    #
    #     print("-----------------结果总览：-------------------------")
    #     print("同步%s条数据" %  count)
    #     print("同步成功%s条数据" % account1)
    #     print("同步失败%s条数据，分别为%s" % (account2,fail))






uc_org_url = "http://117.78.44.16:8721/saveUcOrg"
headers = {"Content-Type": "application/json"}
data = csv.reader(open(r"D:\apache-jmeter-5.1.1\demo\ZY\date\uc_org.csv"))
len1 = []
n = 1
for i in data:
    name = i[0]
    type = i[1]
    subType = i[2]
    shortName = i[3]
    print(i)
    # ur_org = UcOrg(name,type,subType,shortName)
    # ur_org.uc()
    print(name)

    len1.append(name)

    data = {
        "name":name,
        "type":type,
        "subType":subType,
        "shortName":shortName,
        "code":"1",
        "filesNo":"0",
        "address":"成都市",
        "isBuyed":"0",
        "ylAccount":"1",
        "industry":"测试数据",
        "status":"1"
    }
    datas = json.dumps(data)
print(len1)
count = 0
success = []
fail = []
for u in len1:
    count += 1

    r = requests.post(uc_org_url, data=datas, headers=headers) #调用接口（url,参数，类型）
    re= json.loads(r.text) #获取响应数据
    # success = []
    # fail = []


    print("-----------打印请求数据如下：--------------")
    print(json_util.dumps(data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出

    print("---------打印同步数据结果：---------------")
    print(json_util.dumps(re,ensure_ascii=False,indent=4)) #打印响应结果，以json格式输出
    print(r.json) #打印响应状态码
    if r.status_code == 200:
        print("同步数据成功！！！")
        success.append(u)
    else:
        print("同步数据失败！！！")
        fail.append(u)
    account1 = len(success)
    account2 = len(fail)
print("-----------------结果总览：-------------------------")
print("同步%s条数据" %  count)
print("同步成功%s条数据" % account1)
print("同步失败%s条数据，分别为%s" % (account2,fail))

# ur_org = UcOrg(uc_org_url,datas,headers)
# ur_org.uc()