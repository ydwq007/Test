# -*- coding: utf-8 -*-
import requests,json,logging,csv
from bson import json_util
logging.basicConfig(level=logging.DEBUG)



# 导入数据文件，格式CSV
data = csv.reader(open(r"D:\apache-jmeter-5.1.1\demo\ZY\date\uc_org.csv"))
print(type(data))

n = 1
for i in data:
    # print("----------第次打%s印结果如下--------------" % n)
    # print(i) #打印正行数据
    # print(i[0]) #打印指定列
    # print(i) #打印正行数据
    # print(i[0]) #打印指定列
    name = i[0]
    type = i[1]
    subType = i[2]
    shortName = i[3]
    n += 1

uc_org_url = "http://117.78.44.16:8721/saveUcOrg"
headers = {"Content-Type": "application/json"}
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

r = requests.post(uc_org_url, data=datas, headers=headers) #调用接口（url,参数，类型）
re= json.loads(r.text) #获取响应数据


print("-----------打印请求数据如下：--------------")
print(json_util.dumps(data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出

print("---------打印同步数据结果：---------------")
print(json_util.dumps(re,ensure_ascii=False,indent=4)) #打印响应结果，以json格式输出
print(r.json) #打印响应状态码
if r.status_code == 200:
    print("同步数据成功！！！")
else:
    print("同步数据失败！！！")


