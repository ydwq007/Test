# -*- coding: utf-8 -*-
"""
接口：表单活动投票
创建人：魏奇
创建时间：2019-09-12
更新时间：2019-09-12
描述：表单活动投票，一个账号最多投20票，一个表单只能一票
"""

import Json_data,requests
from bson import json_util
import sys
sys.path.append(r"D:\IdeaProjects\seeyon\PyUnittest\TestDatas") #跨目录调用需要配置路径
import BasicDatas

#获取上传表单地址
vote_url = "%s/rest/from_activity/vote" % BasicDatas.test_url_mall

def formvote(Authorization,formid=73):

    data = {
        "form_activity_id":formid
        }

    header = {
        "Content-Type": "application/json",
        "Connection":"keep-alive",
        "Authorization":Authorization
    }
    datas = Json_data.dumps(data)
    #调用接口
    request_baseinfor = requests.post(vote_url, data=datas,headers=header,verify=False) #调用接口（url,参数，类型）#verify=False 跳过认证

    #获取响应数据
    response_formvote= Json_data.loads(request_baseinfor.text)

    print("-----------打印请求数据如下：--------------")
    print(vote_url)
    print(json_util.dumps(data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出

    #打印响应结果，以json格式输出
    print("---------打印响应结果：---------------")
    print(json_util.dumps(response_formvote,ensure_ascii=False,indent=4))
    if response_formvote["code"] == "1000":
        print(json_util.dumps(response_formvote["message"],ensure_ascii=False,indent=4))
        print("表单id为%s，投票成功！！！" % formid)
        return True
    else:
        message = response_formvote["message"]
        print("表单id为%s，投票失败！！！原因为：%s" % (formid,message))
        return False

if __name__ == "__main__":
    # Authorization = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjaG9tZSIsImlhdCI6MTU3MjMxMzY4Mywic2NvcGVzIjoicm9sZV9hY2Nlc3MiLCJleHAiOjE1NzQ5MDU2ODMsInVpZCI6IjE1NjI2NTAzNzUwMTkwMDAwIn0.sQw8OOIALchV6-424ggF3CYriA8p0QW6KRpe_3NkJc8"
    # formvote(Authorization)

    formvote()

