# -*- coding: utf-8 -*-
"""
接口：活动表单上传
创建人：魏奇
创建时间：2019-09-12
更新时间：
描述：上传投票需要的表单和套表
"""

import json,requests
from bson import json_util
import sys
sys.path.append("../../TestDatas") #跨目录调用需要配置路径
import BasicDatas

#获取上传表单地址
upload_url = "%s/rest/from_activity/create" % BasicDatas.test_url_mall

def uploadform(Authorization,data):

    """参数
    {
        "realname": "接口测试套表上传", #真实姓名
        "org_name": "接口测试数据-套表上传", #单位名称
        "mobile": "15982280808", #电话号码
        "type": 2, #上传类型，1表单，2套表
        #表单列表
        "form_list": [{
            "goods_file": "表单名称_1568253714868170000.sfp", #表单文件
            "img_url": "https://test-pic-2-bucket.obs.cn-north-1.myhuaweicloud.com:443"
                       "/%E5%8A%A8%E5%9B%BE_1568253738587170000.gif", #表单图片
            "form_name":"测试套表数据",                  #表单名称type=2 必填
            "domain": "人事管理", #领域
            "desc": "接口测试套表001" #描述
        }
    }
    """
    header = {
        "Content-Type": "application/json",
        "Connection":"keep-alive",
        "Authorization":Authorization
    }
    datas = json.dumps(data)
    #调用接口
    request_baseinfor = requests.post(upload_url, data=datas,headers=header,verify=False) #调用接口（url,参数，类型）#verify=False 跳过认证

    #获取响应数据
    response_uploadform= json.loads(request_baseinfor.text)

    print("-----------打印请求数据如下：--------------")
    print(upload_url)
    print(json_util.dumps(data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出

    #打印响应结果，以json格式输出
    print("---------打印响应结果：---------------")
    print(json_util.dumps(response_uploadform,ensure_ascii=False,indent=4))
    if response_uploadform["code"] == "1000":
        print(json_util.dumps(response_uploadform["message"],ensure_ascii=False,indent=4))
        print("表单上传成功！！！")
        return True
    else:
        message = response_uploadform["message"]
        print("表单上传失败！！！原因为：%s" % message)
        return False

if __name__ == "__main__":
    uploadform()

