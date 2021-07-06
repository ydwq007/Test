# -*- coding: utf-8 -*-
"""
接口：
创建人：魏奇
创建时间：2020-05-07 18:00
描述：
"""

# strs = {"code": "1000", "message": "success", "data": {"returnOrderInfo": {"orderId": "15887446130160000",
#     "orderGoodsId": "1113833", "buyerId": "15730961430270000", "serviceOrgId": "-7422902346933186598",
#     "serviceOrgName": "happy店铺", "goodsName": "2020041001", "goodsPicture": "https://test-pic-2-bucket.obs.cn-north-1.myhuaweicloud.com:443/图2_1573521199093170000.png",
#     "orderGoodsName": None, "orderGoodsPicture": None, "goodsPackageUrl": "更新许可-02_1586508363042170000.syz", "price": 1,
#     "chargingMode": 1, "chargingDuration": "0", "chargingFrequency": "0", "durationUnit": 0, "chargingString": "永久性",
#     "buyerOrgName": "16CRM档案客户名称", "payMethod": "线下通过致远商务订单系统处理", "agencyOrgId": "-2763071546069595220",
#     "agencyOrgName": "21开发环境商家", "returnCode": "15888455240180000", "returnType": 1, "returnTypeStr": "退货",
#     "returnReason": "选错版本", "comment": "正常退货单", "exchangeGoodsName": None, "newOrderGoodsId": None, "returnStatus": 1,
#     "returnStatusStr": "待专属服务机构确认", "orderFinishTime": "2020-05-06 13:57:00", "returnFinishTime": None},
#     "actionList": [{"id": 619, "returnCode": "15888455240180000", "userId": "15730961430270000", "userName": "happy01",
#     "realName": "happy01", "avatars": "https://test-pic-2-bucket.obs.cn-north-1.myhuaweicloud.com:443/avatar419040880_1586698958955170000.png",
#     "returnReason": "选错版本", "comment": "正常退货单", "operationInfo": "订单交易状态：交易完成<br/>退货原因：选错版本<br/>说明：正常退货单",
#     "createUserId": None, "updateUserId": None, "serverCreateTime": "2020-05-07 17:58", "serverUpdateTime": None, "statusFlag": None}]}}
# # # print(type(str))
# # # print(str["data"]["returnOrderInfo"]["orderId"])
#
# # tuple1 = tuple(str)
# # print(type(tuple1))
# # print(tuple1)
#
# tuple2 = tuple(str.values())
# # print(type(tuple2))
# # print(tuple2)
#
# print(type(tuple2[2]))
# print(tuple2[2]["returnOrderInfo"]["returnCode"])
#
#
#
# js = {
#     "orderGoodsId": "1113868",
#     "returnType": "2",
#     "returnReason": "选错版本",
#     "comment": "正常换货单",
#     "orderGoods":{
#         "orderGoodsId":"1113868",
#         "goodsId":"15889221340160000",
#         "goodsName":"196源包backup",
#         "price":"344",
#         "num":"1",
#         "goodsPicture":"https:\/\/testasset.seeyoncloud.com:443\/1_1588750554678.jpg",
#         "shopId":"-6634072791017699823",
#         "shopName":"致远官方旗舰店"
#     }
# }

# js1 = {"code": "1000", "data": {"orderId": "15891788730180000"}, "message": "success"}
# print(js1["data"]["orderId"])
#
#
# # 打印0到1之前的随机数
# from random import random
# print(random())
#
# # 打印指定范围内的随机数
# from random import randint
# print(randint(1,10))


# # 递归
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
#
# print(fact(10))
# a = 1*2*3*4*5*6*7*8*9*10
# print(a)
#
# # 生成器
# def squ(n):
#     i = 1
#     while i <= n:
#         yield i ** 2
#         i += 1
# for i in squ(7):
#     print(i)


# list1 = [
#     {
#         "progress_id":0,
#         "progress_text":"需求沟通",
#         "progress_time":"2020-04-27 13:54:24",
#         "progress_status":1
#     },
#     {
#         "progress_id":1,
#         "progress_text":"应用制作",
#         "progress_time":"",
#         "progress_status":0
#     },
#     {
#         "progress_id":2,
#         "progress_text":"试用安装",
#         "progress_time":"",
#         "progress_status":0
#     },
#     {
#         "progress_id":3,
#         "progress_text":"应用认证",
#         "progress_time":"",
#         "progress_status":0
#     }
# ]


# print(type(list1))
# print(list1)
# import json
# for i in list1:
#     # print(i)
#     if isinstance(i,dict):
#         re_str = json.dumps(i)
#         re_str1 = re_str.encode("utf-8").decode("unicode_escape")
#         print(re_str1)
# # js = dict(list1)
# # print(type(js))
# # print(js)


# a = """["data","order_list",0,"progress_list",0,"progress_time"]#"2020-04-27 13:54:24""""
# print(type(a))
# b = a.split("#")
# print(b)
# # c = eval(b[0])
# c = eval(a.split("#")[0])
# d = eval(a.split("#")[1])
# print(c)
# print(d)
# print(c[0])


# from eliot import start_action, to_file
# to_file(open("eliot.log", "w"))
# def Split1(value,separate):
#     with start_action(action_type="Split", value=value):
#         print(value)
#         Split_list = value.split(separate)
#         print(Split_list)
#         print(eval(Split_list[0]))
#         return Split_list
#
# a = [""Q"#"2020-04-28 13:54:24"",""Q1"#"2020-04-29 13:54:24"",""Q2"#"2020-04-30 13:54:24"",""Q3"*"2020-04-31 13:54:24""]
# for i in a:
#     Split1(i,"#")


# import requests
# from eliot import start_action, to_file

# 1. to_file
# to_file(open("eliot.log", "w"))
#
#
# def check_links(urls):
#     with start_action(action_type="check_links", urls=urls):
#         for url in urls:
#             try:
#                 # 2. start_action
#                 with start_action(action_type="download", url=url):
#                     response = requests.get(url)
#                     response.raise_for_status()
#             except Exception as e:
#                 raise ValueError(str(e))
#
# try:
#     check_links(["http://eliot.readthedocs.io", "http://nosuchurl"])
# except ValueError:
#     print("Not all links were valid.")

# value = [{"progress_id": 0, "progress_text": "需求沟通", "progress_time": "2020-04-27 13:54:24", "progress_status": 1}, {"progress_id": 1, "progress_text": "应用制作", "progress_time": "", "progress_status": 0}, {"progress_id": 2, "progress_text": "试用安装", "progress_time": "", "progress_status": 0}, {"progress_id": 3, "progress_text": "应用认证", "progress_time": "", "progress_status": 0}]
# value1 = """[{"progress_id": 0, "progress_text": "需求沟通", "progress_time": "2020-04-27 13:54:24", "progress_status": 1}, {"progress_id": 1, "progress_text": "应用制作", "progress_time": "", "progress_status": 0}, {"progress_id": 2, "progress_text": "试用安装", "progress_time": "", "progress_status": 0}, {"progress_id": 3, "progress_text": "应用认证", "progress_time": "", "progress_status": 0}]"""
# # value2 = value1.replace("[","")
# # value3 = value2.replace("]","")
# # value4 =value3.replace("},","}#")
# # # print(value4)
# # a = value4.split("#")
# # b = list(value3)
# # print(b)
# # print(type(a))
# # print(type(value))
# a = str(value)
# b = str(value1)
# c = a.replace(""",""")
# print(b == a)
# print(c)
# print(c == b)
# print(value)
# print(a)
# print(list(value1))

# a = [123,"123"]
# b = [123,"123"]
# print(a==b)


# path1 = [["data","order_list",0,"progress_list",0],["data","order_list",0,"progress_list"]]

# # value1 = "2020-04-27 13:54:24"
# # value1 = """{"progress_id": 0, "progress_text": "需求沟通", "progress_time": "2020-04-27 13:54:24", "progress_status": 1}"""
# # value1 = """[{"progress_id": 0, "progress_text": "需求沟通", "progress_time": "2020-04-27 13:54:24", "progress_status": 1}, {"progress_id": 1, "progress_text": "应用制作", "progress_time": "", "progress_status": 0}, {"progress_id": 2, "progress_text": "试用安装", "progress_time": "", "progress_status": 0}, {"progress_id": 3, "progress_text": "应用认证", "progress_time": "", "progress_status": 0}]"""
# value1 = ["""{"progress_id": 0, "progress_text": "需求沟通", "progress_time": "2020-04-27 13:54:24", "progress_status": 1}""","""[{"progress_id": 0, "progress_text": "需求沟通", "progress_time": "2020-04-27 13:54:24", "progress_status": 1}, {"progress_id": 1, "progress_text": "应用制作", "progress_time": "", "progress_status": 0}, {"progress_id": 2, "progress_text": "试用安装", "progress_time": "", "progress_status": 0}, {"progress_id": 3, "progress_text": "应用认证", "progress_time": "", "progress_status": 0}]"""]
#
# for i,j in path1,value1:
#     print(i,j)
#     # print(j)

# for j in range(30,50):
#     print("\033[%s;4m床前明月光，疑是地上霜，举头望明月，低头思故乡。\033[0m 第二行%s" % (j,j))
#     # print("\033[%s;4m床前明月光，疑是地上霜，举头望明月，低头思故乡。" % j)


# # -*- coding: utf-8 -*-
# """
# 接口：通过json匹配值
# 创建人：魏奇
# 更新人：魏奇
# 更新时间：2020-06-11 9:58
# 描述：通过输入相信路径，或者循环匹配的方式查找匹配值
# """
# import json
#
#
#
# # 通过循环检查json中key和值
# match_sign = []
# match_result = []
# def json_loop(jsons, k, v):
#
#     """
#     自定义一个接口测试的方法
#     :param jsons: 需要匹配的源数据
#     :param k: 需要匹配的目标数据的关键字
#     :param v: 需要匹配的目标数据的值
#     """
#
#     # global count
#     # global match_count
#     match_count = 0
#     if isinstance(jsons, dict):  # 判断是否是字典类型isinstance 返回True,false
#
#         dictionary = dict(jsons)
#         for key in dictionary:
#             # print(match_count)
#             if match_count != 0:
#                 break
#             if key == k:
#                 global real_result
#                 real_result = dictionary[key]
#                 # print("\n实际值为：%s" % real_result)
#                 # print(type(v))
#                 if isinstance(v,str) and "#" in v:
#                     # print(True)
#                     new_str = v.split("#")
#                     # print(new_str)
#                     list_str = list(set(new_str))
#                     list_str.sort(key=new_str.index)
#                     for value in list_str:
#                         if value == "":
#                             list_str.remove(value)
#                     if list_str:
#                         real_str = list_str[0]
#                         for i in list_str:
#                             if len(real_str) < len(i):
#                                 real_str = i
#                         if real_str in real_result:
#                             match_count += 1
#                             match_sign.append(True)
#                             break
#                         else:
#                             match_sign.append(False)
#
#                 if real_result == v:
#                     match_count += 1
#                     match_sign.append(True)
#                     break
#                 else:
#                     match_sign.append(False)
#             elif isinstance(dictionary[key], list):
#                 for i in dictionary[key]:
#                     if isinstance(i, dict):
#                         json_loop(i, k, v)
#                         if match_sign[-1]:
#                             break
#             elif isinstance(dictionary[key], dict):
#                 json_loop(dictionary[key], k, v)
#
#         # print(sign)
#         # print(match_sign)
#         # print(real_result)
#         if match_sign and True in match_sign:
#             # return True, real_result
#             if match_sign[-1]:
#                 return True, real_result
#             else:
#                 return False, real_result
#         elif match_sign and True not in match_sign:
#             return False, real_result
#     else:
#         print("匹配的源数据不为字典类型，请重新输入")
#         return False
#
#
#
#
# def json_check(jsons, data):
#
#     """
#     自定义一个接口测试的方法
#     :param jsons: 需要匹配的源数据
#     :param data: 需要匹配的目标数据
#     """
#     count = 1
#     sign = []
#     if isinstance(data, dict):  # 判断是否是字典类型isinstance 返回True,false
#         Except = dict(data)  # 转为字典
#     else:
#         Except = json.loads(data)
#     for key in Except.keys():
#         if Except[key] == "***":  # 适合响应值是动态的，无法通过固定值进行匹配，动态值需要放在最前面进行匹配，否则会报错
#             # 获取动态值
#             check = json_loop(jsons, key, Except[key])
#             # print(check)
#             print("第%s循环检查点，循环匹配成功。key为%s，值为动态值，值为%s" % (count, key, check[1]))
#             # print("第%s循环检查点，循环匹配成功。key为%s，值为动态值" % (count, key))
#             sign.append(True)
#         else:
#             check = json_loop(jsons, key, Except[key])  # 调用循环匹配
#             # print(check)
#             # 打印结果
#             if check:
#                 if check[0]:
#                     print("第%s循环检查点，循环匹配成功。key为%s，期望值为：%s，实际值为：%s" % (count, key, Except[key], check[1]))
#                     sign.append(True)
#                 else:
#                     print("第%s循环检查点，循环匹配失败。key为%s，期望值为：%s，实际值为：%s" % (count, key, Except[key], check[1]))
#                     sign.append(False)
#             else:
#                 print("第%s循环检查点，循环匹配失败。key为%s，期望值为：%s，实际值为：%s" % (count, key, Except[key], None))
#                 sign.append(False)
#         count += 1
#     return sign
#
#
# if __name__ == "__main__":
#
#     json1 = {"code1": "1000", "data": {"code": -1, "data": "", "message": "商品：0520-线下商品-非0元,未匹配到适配版本,请更换商品或联系平台管理员"}, "code": -11, "message": "success"}
#     data1 = """{"code": -11,"message": "商品：0520-线下商品-非0元,未匹配到适配版本,请更换商品或联系平台管理员"}"""
#
#     json2 = {"code": "1000", "data": {"code": 0, "data": {"order_id": "159368041101600001", "order_no": "159368041101600002","code": 10,"message": "success1"}, "message": "订单创建成功"}, "message": "success"}
#     data2 = """{"code": 10, "message": "success","order_id": "159368041101600002"}"""   #"""{"order_id": "***","code": 10, "message": "success"}"""
#
#     json3 = {"code": "1000", "data": {"code": -1, "data": "", "message": "商品：0520-线下商品-非0元,未匹配到适配版本,请更换商品或联系平台管理员"}, "message1": "success"}
#     data3 = """{"code": -1, "message": "商品：###,未匹配到适配版本,请更换商品或联系#,平台管理员","message1": "success"}"""
#     # data3_1 = """{ "message": "商品：0520-线下商品-非0元,未匹配到适配版本,请更换商品或联系###,平台管理员"}"""
#
#
#     json_value = json3
#     data = data3
#
#     json_check(json_value, data)

    # [["data","message"],["data","code"]]#["商品：0520-线下商品-非0元,未匹配到适配版本,请更换商品或联系平台管理员",-1]

#
# # str1 = ".为保障您的权益，您购买的平台商品期限须大于等于其他非平台商品的期限，请调整后再购买!商品:0520-线上-商品"
# # str2 = "为保障您的权益，您购买的平台商品期限须大于等于其他非平台商品的期限，请调整后再购买!商品:###."
# # str3 = "商品：.为保障您的权益，您购买的平台商品期限须大于等于其他非平台商品的期限，请调整后再购买!"
# #
# # except_str = str3
# # # if "#," in str4 or "#." in str4 or "#，" in str4 or "#。" in str4 or ":#" in str4 or "：#" in str4:
# # if "#" in except_str:
# #     # print(True)
# #     new_str = except_str.split("#")
# #     # print(new_str)
# #     list_str = list(set(new_str))
# #     list_str.sort(key=new_str.index)
# #     for value in list_str:
# #         if value == "":
# #             list_str.remove(value)
# #     print(list_str)
# #     if list_str:
# #         real_str = list_str[0]
# #         for i in list_str:
# #             if len(real_str) < len(i):
# #                 real_str = i
# #     else:
# #         real_str = "不存在"
# #     print(real_str)
# # else:
# #     print(False)
# #     real_str = "不存在"
# #
# # if real_str in str1:
# #     print(True)
# # else:
# #     print(False)
# # # print(str2 < str1)


# a1 = "23213213"
# if isinstance(a1, str):
#     print(1)
# else:
#     print(2)

# import json
# json5 = """{"code": 1000, "message": "success", "data": [{"id": 78, "permission_name": "短信通知", "permission_mark": "admin-shortMessage", "permission_url": "/admin/order/mobileNotify", "pid": 77, "permission_type": 1, "is_permission": 0, "child": []}, {"id": 79, "permission_name": "订单列表", "permission_mark": "admin-orderList", "permission_url": "/admin/order/orderlist", "pid": 77, "permission_type": 1, "is_permission": 0, "child": [{"id": 84, "permission_name": "供应商订单", "permission_mark": "admin-order-supply", "permission_url": "", "pid": 79, "permission_type": 2, "is_permission": 0, "child": []}, {"id": 85, "permission_name": "服务商订单", "permission_mark": "admin-order-service", "permission_url": "", "pid": 79, "permission_type": 2, "is_permission": 0, "child": []}, {"id": 86, "permission_name": "经销商订单", "permission_mark": "admin-order-agency", "permission_url": "", "pid": 79, "permission_type": 2, "is_permission": 0, "child": []}, {"id": 87, "permission_name": "导出数据", "permission_mark": "admin-orderExport", "permission_url": "", "pid": 79, "permission_type": 3, "is_permission": 0, "child": []}, {"id": 88, "permission_name": "订单详情", "permission_mark": "admin-orderDetail", "permission_url": "", "pid": 79, "permission_type": 3, "is_permission": 0, "child": []}, {"id": 89, "permission_name": "确认订单", "permission_mark": "admin-orderconfirm", "permission_url": "", "pid": 79, "permission_type": 3, "is_permission": 0, "child": []}, {"id": 90, "permission_name": "取消订单", "permission_mark": "admin-orderclose", "permission_url": "", "pid": 79, "permission_type": 3, "is_permission": 0, "child": []}, {"id": 91, "permission_name": "删除订单", "permission_mark": "admin-orderdel", "permission_url": "", "pid": 79, "permission_type": 3, "is_permission": 0, "child": []}, {"id": 112, "permission_name": "页面展示", "permission_mark": "admin-showOrderList", "permission_url": "", "pid": 79, "permission_type": 1, "is_permission": 0, "child": []}]}, {"id": 80, "permission_name": "定制单列表", "permission_mark": "admin-customList", "permission_url": "/admin/html/Customize-index", "pid": 77, "permission_type": 1, "is_permission": 0, "child": [{"id": 81, "permission_name": "确认订单", "permission_mark": "admin-customConfirm", "permission_url": "", "pid": 80, "permission_type": 3, "is_permission": 0, "child": []}, {"id": 82, "permission_name": "删除订单", "permission_mark": "admin-customDel", "permission_url": "", "pid": 80, "permission_type": 3, "is_permission": 0, "child": []}, {"id": 83, "permission_name": "指定设计师", "permission_mark": "admin-customDesign", "permission_url": "", "pid": 80, "permission_type": 3, "is_permission": 0, "child": []}, {"id": 113, "permission_name": "页面展示", "permission_mark": "admin-showCustomList", "permission_url": "", "pid": 80, "permission_type": 1, "is_permission": 0, "child": []}]}, {"id": 15832944070160000, "permission_name": "退换货管理", "permission_mark": "admin-Exchange-list", "permission_url": "/admin/html/Exchange-list", "pid": 77, "permission_type": 1, "is_permission": 0, "child": [{"id": 15832945270160000, "permission_name": "退换货详情", "permission_mark": "order_exchange_detail", "permission_url": "/admin/html/Exchange-detail", "pid": 15832944070160000, "permission_type": 1, "is_permission": 0, "child": []}, {"id": 15833089210160000, "permission_name": "页面", "permission_mark": "order_Exchange_list", "permission_url": "", "pid": 15832944070160000, "permission_type": 1, "is_permission": 0, "child": []}]}]}"""
# print(type(json5))
#
# print(json.loads(json5))


# s = ""
# print(type(s))
# print(s)
# if s is None:
#     print(True)
# else:
#     print(False)
#
# if s is "":
#     print(True)
# else:
#     print(False)
#
# if len(s) == 0:
#     print(True)
# else:
#     print(False)

a = [1, 2, 3, 4]
b = ["A", "B", "C", "D"]
c = ["甲", "乙", "丙", "丁"]
d = zip(a, b, c)

# for i, j, h in d:
#     print("\n第%s个值为%s" % (i, j))
#     print("第{}个值为{}".format(i, j))
#     print("第{0}个值为{1}".format(i, h))
#
# a1 = []
# for i in range(10):
#     a1.append(i)
# print(a1)
#
# x = []
# a = [[1,2],[3,4],[5,6]]
# for i in a:
#     print(i)
#     for j in i:
#         print(j)
#         x.append(j)
#
# print(x)
#
# import numpy as np
# a = [[1,2],[3,4],[5,6]]
# b = np.array(a).flatten().tolist()
# print(b)


# a = ""
# print(type(a))
# print(a)
#
# b = None
# print(type(b))
# print(b)

# c = ["",None]
# print(c[0])
# print(c[1])
# print(type(c[0]))
# print(type(c[1]))


