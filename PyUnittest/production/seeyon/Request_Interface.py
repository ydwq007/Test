# -*- coding: utf-8 -*-
"""
接口：请求接口
创建人：魏奇
更新人：魏奇
更新时间：2019-11-20 17:28
描述：
"""

import requests
import Execute_Log as log
import Json_data

logging = log.get_logger()

def change_type(value):
    """
    对dict类型进行中文识别
    :param value: 传的数据值
    :return: 转码后的值
    """
    try:
        if isinstance(eval(value), str):
            return value
        if isinstance(eval(value), dict):
            result = eval(Json_data.dumps(value))
            return result
    except Exception as e:
        logging.error("类型问题 %s", e)


def api(method, url, data ,headers):
    """
    自定义一个接口测试的方法
    :param method: 请求类型
    :param url: 地址
    :param data: 数据
    :param headers: 请求头
    :return: code码
    """
    global results
    try:
        if method == ("post" or "POST"):
            results = requests.post(url=url, data=data, headers=headers,verify=False)
        if method == ("get" or "GET"):
            results = requests.get(url=url, data=data, headers=headers,verify=False)
        # if method == "put":
        #     results = requests.put(url, data, headers=headers)
        # if method == "delete":
        #     results = requests.delete(url, headers=headers)
        # if method == "patch":
        #     results == requests.patch(url, data, headers=headers)
        # if method == "options":
        #     results == requests.options(url, headers=headers)
        # response = results.json()
        print(results)
        response = Json_data.loads(results.text) #json.loads()用于将字符串形式的数据转化为字典
        print(response)
        code = response.get("code")
        return code
    except Exception as e:
        logging.error("service is error", e)


def content(method, url, data, headers):
    """
    请求response自己可以自定义检查结果
    :param method: 请求类型
    :param url: 请求地址
    :param data: 请求参数
    :param headers: 请求headers
    :return: message信息
    """
    global results
    try:
        if method == ("post" or "POST"):
            results = requests.post(url, data, headers=headers)
        if method == ("get" or "GET"):
            results = requests.get(url, data, headers=headers)
        if method == ("put" or "PUT"):
            results = requests.put(url, data, headers=headers)
        if method == ("patch" or "PATCH"):
            results = requests.patch(url, data, headers=headers)
        response = results.json()
        message = response.get("message")
        result = response.get("result")
        content = {"message": message, "result": result}
        return content
    except Exception as e:
        logging.error("请求失败 %s" % e)