# -*- coding: utf-8 -*-
"""
接口：获取图形验证码，并解析
创建人：魏奇
更新人：魏奇
更新时间：2019-11-20 14:11
描述：
"""

import requests,json,sys
from bson import json_util
sys.path.append('../../TestDatas') #跨目录调用需要配置路径
import BasicDatas
# # logging.basicConfig(level=logging.DEBUG)

class Captcha():

    def __init__(self,chome):
        #参数化
        self.chome = chome

    def get_Captcha(self):


        #获取图像验证码地址
        get_Captcha_url = "%s/portal.php?m=util&a=randcode&type=login&w=90&h=40&base64=1" % self.chome

        #调用请求
        request_get_Captcha = requests.get(get_Captcha_url,headers=BasicDatas.headers, verify=False) #调用接口（url,参数，类型）#verify=False 跳过认证

        #获取响应数据
        response_get_Captcha= json.loads(request_get_Captcha.text) #son.loads()用于将字符串形式的数据转化为字典

        print("获取图像验证码地址：%s" % get_Captcha_url)
        print("获取图像验证码响应结果为：\n%s" % json_util.dumps(response_get_Captcha,ensure_ascii=False,indent=4)) #打印响应数据，以json格式输出

        if response_get_Captcha["code"] == "1000":
            imgcode = response_get_Captcha["imgCode"]
            print("获取图形验证成功！！！结果为：\n%s" % imgcode)
            print(type(imgcode))


if __name__ == "__main__":
    test = Captcha(BasicDatas.test_chome)
    test.get_Captcha()