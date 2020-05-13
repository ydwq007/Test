# -*- coding: utf-8 -*-
"""
接口：解析json
创建人：魏奇
更新人：魏奇
更新时间：2019-12-18 18:16
描述：
"""
import json
from collections import Counter #使用collections模块下的Counter类


# 检查json中key和值
sign = []
def json_check(jsons,k,v):
    global count
    count = 0
    if isinstance(jsons,dict): # 判断是否是字典类型isinstance 返回True,false
        dictionary = dict(jsons)
        for key in dictionary:
            if key == k:
                if dictionary[key] == v:
                    # print("key为%s,值为%s" % (key,dictionary[key]))
                    # print(True)
                    sign.append(True)
                    count +=  1
                    break
                    # return True,key,dictionary[key]
                else:
                    sign.append(False)
                    # return False,key,dictionary[key]
            elif isinstance(dictionary[key],list):
                # print(dictionary[key])
                for i in dictionary[key]:
                    # print(type(i))
                    # print(i)
                    # json_check(i,k,v)
                    if isinstance(i,dict):
                        json_check(i,k,v)
            elif isinstance(dictionary[key],dict):
                json_check(dictionary[key],k,v)

    # account = Counter(sign) #使用Counter，统计匹配成功的次数
    # print(account)

    # account = set(sign) #使用集合，统计匹配测试
    # result = {}
    # for item in account:
    #     result.update({item:sign.count(item)})
    # print(result)

    if sign and True in sign:
        if count >= 1:
            return True
    else:
        return False


if __name__ == "__main__":
    import json
    json1 = {
        "code": 1000,
        "data": {
            "uid": "156344254701900001",
            "mobile": "15982286537",
            "token": {
                "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjaG9tZSIsImlhdCI6MTU3NjY2MzU5Nywic2NvcGVzIjoicm9sZV9hY2Nlc3MiLCJleHAiOjE1NzkyNTU1OTcsInVpZCI6IjE1NjM0NDI1NDcwMTkwMDAwIn0.5aKSmTyB-riy-RqbSarWfPBlGMqqwfinO1mN1TtF81o", "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjaG9tZSIsImlhdCI6MTU3NjY2MzU5Nywic2NvcGVzIjoicm9sZV9yZWZyZXNoIiwiZXhwIjoxNTc5MzQxOTk3LCJ1aWQiOiIxNTYzNDQyNTQ3MDE5MDAwMCJ9.ZIaHM2boqnuwvuRf4TW2vq08jBltQVzNnjWb1xeJrNI",
                "token_type": "bearer",
                "uid": "15634425470190000"
            }
        },
        "message": "",
        "uid": "156344254701900001",
        "mobile": "159822865371"
    }


    data1 = """{"mobile": "15982286537","uid": "15634425470190000"
            }"""


    json2 = {"code": "1000", "message": "success", "data": {"returnOrderInfo": {"orderId": "15890134720160000", "orderGoodsId": "1113896", "buyerId": "15730961430270000", "serviceOrgId": "-6634072791017699823", "serviceOrgName": "致远官方旗舰店", "goodsName": "196源包backup", "goodsPicture": "https://testasset.seeyoncloud.com:443/TIM%E5%9B%BE%E7%89%8720200113174521_1588922072827.gif", "orderGoodsName": None, "orderGoodsPicture": None, "goodsPackageUrl": "196源包backup第一次升级增加无流程_backup_1588922709763.syz", "price": 10, "chargingMode": 1, "chargingDuration": "0", "chargingFrequency": "0", "durationUnit": 0, "chargingString": "永久性", "buyerOrgName": "16CRM档案客户名称", "payMethod": "线下通过致远商务订单系统处理", "agencyOrgId": "-2763071546069595220", "agencyOrgName": "21开发环境商家", "returnCode": "15891625190180000", "returnType": 2, "returnTypeStr": "换货", "returnReason": "选错版本", "comment": "", "exchangeGoodsName": "20200506-16", "newOrderGoodsId": None, "returnStatus": 1, "returnStatusStr": "待专属服务机构确认", "orderFinishTime": "2020-05-09 16:38:01", "returnFinishTime": None}, "actionList": [{"id": 798, "returnCode": "15891625190180000", "userId": "15730961430270000", "userName": "happy01", "realName": "happy01", "avatars": "https://test-pic-2-bucket.obs.cn-north-1.myhuaweicloud.com:443/avatar419040880_1586698958955170000.png", "returnReason": "选错版本", "comment": "", "operationInfo": "订单交易状态：交易完成<br/>换货原因：选错版本<br/>换货为：20200506-16<br/>说明：", "createUserId": None, "updateUserId": None, "serverCreateTime": "2020-05-11 10:01", "serverUpdateTime": None, "statusFlag": None}]}}
    data2 = """{"orderId": "15890134720160000","returnStatusStr": "待专属服务机构确认","code": "1000"}"""

    json3 = {"code":0,"data":{"actionList":[{"avatars":"https://test-pic-2-bucket.obs.cn-north-1.myhuaweicloud.com:443/avatar419040880_1586698958955170000.png","comment":"","id":800,"operationInfo":"订单交易状态：交易完成<br/>退货原因：选错版本<br/>说明：","realName":"happy01","returnCode":15891637940180000,"returnReason":"选错版本","serverCreateTime":1589163794677,"userId":15730961430270000,"userName":"happy01"}],"returnOrderInfo":{"agencyOrgId":-2763071546069595220,"agencyOrgName":"21开发环境商家","buyerId":15730961430270000,"buyerOrgName":"16CRM档案客户名称","chargingDuration":"0","chargingFrequency":"0","chargingMode":1,"chargingString":"永久 性","comment":"","durationUnit":0,"goodsName":"nancytest0530","goodsPackageUrl":"自定义控件_1559204282170680000.syz","goodsPicture":"https://test-pic-2-bucket.obs.cn-north-1.myhuaweicloud.com:443/39jpg_1559204316145680000.jpg","orderFinishTime":"2020-05-11 10:22:56","orderGoodsId":1113907,"orderId":15891637670160000,"payMethod":"线下通过致远商务订单系统处理","price":222.0,"returnCode":15891637940180000,"returnReason":"选错版本","returnStatus":1,"returnStatusStr":"待专属服务机构确认","returnType":1,"returnTypeStr":"退货","serviceOrgId":3822076186310298662,"serviceOrgName":"GJX01店铺"}},"message":"成功"}
    data3 = """{"returnCode":15891637940180000,"returnStatusStr": "待专属服务机构确认","code": 0}"""

    json4 = {"code": "1000", "message": "success", "data": {"total": 1, "list": [{"orderId": "15867735860160000", "orderGoodsId": None, "buyerId": None, "oldGoodsName": "2020041001", "oldGoodsPicture": "https://test-pic-2-bucket.obs.cn-north-1.myhuaweicloud.com:443/图2_1573521199093170000.png", "oldPrice": 1, "oldNum": 1, "oldServiceOrgName": "happy店铺", "newGoodsName": None, "newGoodsPicture": None, "newPrice": None, "newNum": None, "newServiceOrgName": None, "buyerOrgId": "7011822724667952339", "buyerOrgName": "16CRM档案客户名称", "agencyOrgId": "-2763071546069595220", "agencyOrgName": "21开发环境商家", "returnCode": "15887309280180000", "returnType": 1, "returnTypeStr": "退货", "returnStatus": 3, "newReturnStatus": None, "returnStatusStr": "退货成功", "creatTime": "2020-05-06 10:08", "orderFinishTime": "2020-04-13 18:27", "returnFinishTime": "2020-05-06 13:49", "licenseUpdateTime": "2020-05-06 08:40", "goodsExpireDate": None, "licenseUpdateFlag": False, "goodsExpireFlag": False, "goodsPackageCertificateUrl": None}], "pageNum": 1, "pageSize": 1, "size": 1, "startRow": 0, "endRow": 0, "pages": 1, "prePage": 0, "nextPage": 0, "isFirstPage": True, "isLastPage": True, "hasPreviousPage": False, "hasNextPage": False, "navigatePages": 8, "navigatepageNums": [1], "navigateFirstPage": 1, "navigateLastPage": 1, "firstPage": 1, "lastPage": 1}}
    data4 = """{"code": "1000", "message": "success", "orderId": "15867735860160000"}"""

    json_value = json1
    data = data1

    print(type(json_value))
    # print(json_value)
    print(type(data))
    Except = json.loads(data)
    # print(data)


    si = []
    for key in Except.keys():
        check = json_check(json_value,key,Except[key])
        # print(check)
        if check == True:
            print("检查成功。key为%s，值为%s" % (key,Except[key]))
        else:
            print("检查失败。key为%s，值为%s" % (key,Except[key]))





    # print(Except)
    # check1 = json_check1(json1,Except) #字符串校对
    # print(check1)
    # if check1 == True:
    #     print("检查成功。检查字符串为%s" % Except)
    # else:
    #     print("检查失败。检查字符串为%s" % Except)


