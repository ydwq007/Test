# -*- coding: utf-8 -*-
"""
接口：通过json匹配值
创建人：魏奇
创建时间：2020-06-11 9:58
描述：通过输入相信路径，或者循环匹配的方式查找匹配值
"""
import json


# 通过json的key值具体路径匹配值
def json_path(result1, except_path, except_value):

    """
    自定义一个接口测试的方法
    :param result1: 需要匹配的源数据
    :param except_path: 需要匹配的目标数据的路径，传入的是列表list，一层一个值，如["data","returnOrderInfo","orderGoodsId"]，代表
    {"data": {"returnOrderInfo": {"orderId": "15890134720160000"}}}
    :param except_value: 需要匹配的目标数据的值
    """
    compare_sign = []
    sign, re_sign = [], []
    for j in range(len(except_path)):
        path = except_path[j]
        value = except_value[j]
        result = result1
        for i in range(len(path)):
            result = result[path[i]]
            # 返回结果为字典转换为字符串
            if isinstance(result, dict):  # 判断是否是字典类型isinstance 返回True,false
                re_str = json.dumps(result)
                re_str1 = re_str.encode("utf-8").decode("unicode_escape")
            elif isinstance(result, list):
                re_str2 = str(result)
                re_str1 = re_str2.replace("'", "'")
            else:
                re_str1 = result

            # 比较字符串和预期值
            if re_str1 == value:
                sign.append(True)
            else:
                sign.append(False)

        # 判断单个路径最终值是否匹配
        if sign[-1]:
            print("第%s路径检查点，路径匹配成功，期望值为：%s，实际值为：%s" % (j+1, value, re_str1))
            re_sign.append(True)
            # break
        else:
            print("第%s路径检查点，路径匹配失败，期望值为：%s，实际值为：%s" % (j+1, value, re_str1))
            re_sign.append(False)

    # 整个期望值判断
    if re_sign and False not in re_sign:
        compare_sign.append(True)
    else:
        compare_sign.append(False)

    return compare_sign, re_sign, sign


# 通过循环检查json中key和值
match_sign = []
def json_loop(jsons, k, v):

    """
    自定义一个接口测试的方法
    :param jsons: 需要匹配的源数据
    :param k: 需要匹配的目标数据的关键字
    :param v: 需要匹配的目标数据的值，如果实际值为None，期望值需要填写为null
    """

    global match_count
    match_count = 0
    if isinstance(jsons, dict):  # 判断是否是字典类型isinstance 返回True,false
        dictionary = dict(jsons)
        for key in dictionary:
            if match_count != 0:
                break
            if key == k:
                global real_result
                real_result = dictionary[key]
                # 匹配字符串中有动态值
                if isinstance(v,str) and "#" in v:
                    new_str = v.split("#")
                    list_str = list(set(new_str))
                    list_str.sort(key=new_str.index)
                    for value in list_str:
                        if value == "":
                            list_str.remove(value)
                    if list_str:
                        real_str = list_str[0]
                        for i in list_str:
                            if len(real_str) < len(i):
                                real_str = i
                        if real_str in real_result:
                            match_count += 1
                            match_sign.append(True)
                            break
                        else:
                            match_sign.append(False)

                # 匹配固定值
                if real_result == v:
                    match_count += 1
                    match_sign.append(True)
                    break
                else:
                    match_sign.append(False)
            elif isinstance(dictionary[key], list):
                for i in dictionary[key]:
                    if isinstance(i, dict):
                        json_loop(i, k, v)
                        if match_sign[-1]:
                            break
            elif isinstance(dictionary[key], dict):
                json_loop(dictionary[key], k, v)

        if match_sign:
            if match_sign[-1]:
                return True, real_result
            else:
                return False, real_result
        else:
            return False, real_result
    else:
        print("匹配的源数据不为字典类型，请重新输入")
        return False, json




def json_check(jsons, data):

    """
    自定义一个接口测试的方法
    :param jsons: 需要匹配的源数据
    :param data: 需要匹配的目标数据
    """
    count = 1
    sign = []
    if isinstance(data, dict):  # 判断是否是字典类型isinstance 返回True,false
        Except = dict(data)  # 转为字典
    else:
        Except = json.loads(data)
    for key in Except.keys():
        if Except[key] == "***":  # 适合响应值是动态的，无法通过固定值进行匹配
            # 获取动态值
            check = json_loop(jsons, key, Except[key])
            print("第%s循环检查点，循环匹配成功。key为%s，值为动态值，值为%s" % (count, key, check[1]))
            sign.append(True)
        else:
            check = json_loop(jsons, key, Except[key])  # 调用循环匹配
            # 打印结果
            if check:
                if check[0]:
                    print("第%s循环检查点，循环匹配成功。key为%s，期望值为：%s，实际值为：%s" % (count, key, Except[key], check[1]))
                    sign.append(True)
                else:
                    print("第%s循环检查点，循环匹配失败。key为%s，期望值为：%s，实际值为：%s" % (count, key, Except[key], check[1]))
                    sign.append(False)
            else:
                print("第%s循环检查点，循环匹配失败。key为%s，期望值为：%s，实际值为：%s" % (count, key, Except[key], None))
                sign.append(False)
        count += 1
    return sign


if __name__ == "__main__":

    # 通过循环匹配
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

    json3 = {"code": 0, "data": {"actionList": [{"avatars": "https://test-pic-2-bucket.obs.cn-north-1.myhuaweicloud.com:443/avatar419040880_1586698958955170000.png","comment":"","id":800,"operationInfo":"订单交易状态：交易完成<br/>退货原因：选错版本<br/>说明：","realName":"happy01","returnCode":15891637940180000,"returnReason":"选错版本","serverCreateTime":1589163794677,"userId":15730961430270000,"userName":"happy01"}],"returnOrderInfo":{"agencyOrgId":-2763071546069595220,"agencyOrgName":"21开发环境商家","buyerId":15730961430270000,"buyerOrgName":"16CRM档案客户名称","chargingDuration":"0","chargingFrequency":"0","chargingMode":1,"chargingString":"永久 性","comment":"","durationUnit":0,"goodsName":"nancytest0530","goodsPackageUrl":"自定义控件_1559204282170680000.syz","goodsPicture":"https://test-pic-2-bucket.obs.cn-north-1.myhuaweicloud.com:443/39jpg_1559204316145680000.jpg","orderFinishTime":"2020-05-11 10:22:56","orderGoodsId":1113907,"orderId":15891637670160000,"payMethod":"线下通过致远商务订单系统处理","price":222.0,"returnCode":15891637940180000,"returnReason":"选错版本","returnStatus":1,"returnStatusStr":"待专属服务机构确认","returnType":1,"returnTypeStr":"退货","serviceOrgId":3822076186310298662,"serviceOrgName":"GJX01店铺"}},"message":"成功"}
    data3 = """{"returnCode":15891637940180000,"returnStatusStr": "待专属服务机构确认","code": 0}"""

    json4 = {"code": "1000", "message": "success", "data": {"total": 1, "list": [{"orderId": "15867735860160000", "orderGoodsId": None, "buyerId": None, "oldGoodsName": "2020041001", "oldGoodsPicture": "https://test-pic-2-bucket.obs.cn-north-1.myhuaweicloud.com:443/图2_1573521199093170000.png", "oldPrice": 1, "oldNum": 1, "oldServiceOrgName": "happy店铺", "newGoodsName": None, "newGoodsPicture": None, "newPrice": None, "newNum": None, "newServiceOrgName": None, "buyerOrgId": "7011822724667952339", "buyerOrgName": "16CRM档案客户名称", "agencyOrgId": "-2763071546069595220", "agencyOrgName": "21开发环境商家", "returnCode": "15887309280180000", "returnType": 1, "returnTypeStr": "退货", "returnStatus": 3, "newReturnStatus": None, "returnStatusStr": "退货成功", "creatTime": "2020-05-06 10:08", "orderFinishTime": "2020-04-13 18:27", "returnFinishTime": "2020-05-06 13:49", "licenseUpdateTime": "2020-05-06 08:40", "goodsExpireDate": None, "licenseUpdateFlag": False, "goodsExpireFlag": False, "goodsPackageCertificateUrl": None}], "pageNum": 1, "pageSize": 1, "size": 1, "startRow": 0, "endRow": 0, "pages": 1, "prePage": 0, "nextPage": 0, "isFirstPage": True, "isLastPage": True, "hasPreviousPage": False, "hasNextPage": False, "navigatePages": 8, "navigatepageNums": [1], "navigateFirstPage": 1, "navigateLastPage": 1, "firstPage": 1, "lastPage": 1}}
    data4 = """{"code": "1000", "message": "success", "orderId": "15867735860160000","oldGoodsName": "2020041001"}"""

    json5 = {"code": "1000", "message": "success", "data": {"returnOrderInfo": {"orderId": "158890179701600001", "orderGoodsId": "1113856", "buyerId": "15730961430270000", "serviceOrgId": "-7422902346933186598", "serviceOrgName": "happy店铺", "goodsName": "2020041001", "goodsPicture": "https://test-pic-2-bucket.obs.cn-north-1.myhuaweicloud.com:443/图2_1573521199093170000.png", "orderGoodsName": None, "orderGoodsPicture": None, "goodsPackageUrl": "更新许可-02_1586508363042170000.syz", "price": 1, "chargingMode": 1, "chargingDuration": "0", "chargingFrequency": "0", "durationUnit": 0, "chargingString": "永久性", "buyerOrgName": "16CRM档案客户名称", "payMethod": "线下通过致远商务订单系统处理", "agencyOrgId": "-2763071546069595220", "agencyOrgName": "21开发环境商家", "returnCode": "15893765730180001", "returnType": 1, "returnTypeStr": "退货", "returnReason": "选错版本", "comment": "", "exchangeGoodsName": None, "newOrderGoodsId": None, "returnStatus": 1, "returnStatusStr": "待专属服务机构确认", "orderFinishTime": "2020-05-08 09:37:17", "returnFinishTime": None}, "actionList": [{"id": 873, "returnCode": "15893765730180001", "userId": "15730961430270000", "userName": "happy01", "realName": "happy01", "avatars": "https://test-pic-2-bucket.obs.cn-north-1.myhuaweicloud.com:443/avatar419040880_1586698958955170000.png", "returnReason": "选错版本", "comment": "", "operationInfo": "订单交易状态：交易完成<br/>退货原因：选错版本<br/>说明：", "createUserId": None, "updateUserId": None, "serverCreateTime": "2020-05-13 21:29", "serverUpdateTime": None, "statusFlag": None}]}}
    data5 = """{ "orderId": "15889017970160000","code": "1000", "message": "success","buyerId": "157309614302700001","orderGoodsId":"***"} """

    json6 = {"code": 1000, "message": "success", "data": {"total": "90", "num": "20", "items": [{"credit_no": "91330100609136098C", "reg_no": "330100000109245", "oper_name": "宗庆后", "name": "杭州娃哈哈食品有限公司", "id": "b6d98c2a-9252-4a11-b230-c32955276ea3", "start_date": "1992-10-28"}, {"credit_no": "913502007516496951", "reg_no": "350200400001921", "oper_name": "宗馥莉", "name": "厦门娃哈哈食品有限公司", "id": "788a1431-73ff-4284-a891-50ba27cf6768", "start_date": "2004-07-21"}, {"credit_no": "91120222797277364P", "reg_no": "120000400008125", "oper_name": "何卫冰", "name": "天津娃哈哈食品有限公司", "id": "95dca192-504f-4363-b7dd-2d04ceed884c", "start_date": "2007-02-13"}, {"credit_no": "91360100792833085D", "reg_no": "360100510001326", "oper_name": "金文来", "name": "南昌娃哈哈食品有限公司", "id": "dafa57f7-46ef-4e2b-986b-6e2c1e0e8c74", "start_date": "2006-09-28"}, {"credit_no": "91510800MA62552B3T", "reg_no": "510000400000788", "oper_name": "宗庆后", "name": "广元娃哈哈食品有限公司", "id": "11e18a78-84ab-48e0-954d-5f9905ab2955", "start_date": "1999-03-31"}, {"credit_no": "91620000719024409C", "reg_no": "620000400000265", "oper_name": "宗庆后", "name": "天水娃哈哈食品有限公司", "id": "5780674a-b276-43b7-9774-98858f9a11eb", "start_date": "2000-10-27"}, {"credit_no": "912101007643905120", "reg_no": "210100400001383", "oper_name": "戚列心", "name": "沈阳娃哈哈食品有限公司", "id": "631e74c2-ce48-47bb-8fd5-b3c25ddc0690", "start_date": "2004-11-19"}, {"credit_no": "91220201724865712L", "reg_no": "220200400002714", "oper_name": "宗庆后", "name": "吉林娃哈哈食品有限公司", "id": "36e255b5-c741-4741-b669-3474712b6c1f", "start_date": "2000-10-18"}, {"credit_no": "91370700780796985N", "reg_no": "370700400010651", "oper_name": "宗庆后", "name": "潍坊娃哈哈食品有限公司", "id": "6c3b25c8-0a2e-45d1-b932-fa947198d49a", "start_date": "2005-11-23"}, {"credit_no": "914113007457905297", "reg_no": "411300400000537", "oper_name": "宗庆后", "name": "南阳娃哈哈食品有限公司", "id": "3d6b25a2-9554-496e-bc41-2d70b9b0b5c6", "start_date": "2003-02-09"}, {"credit_no": "91610400770017300X", "reg_no": "610400400000773", "oper_name": "宗庆后", "name": "陕西娃哈哈食品有限公司", "id": "becc0d26-f92c-4789-874a-f3c5c3b05bcf", "start_date": "2005-01-26"}, {"credit_no": "-", "reg_no": "430100400002410", "oper_name": "宗馥莉", "name": "长沙娃哈哈食品有限公司", "id": "acd0a1bb-4fb2-48eb-8de8-b62c472931b5", "start_date": "1999-11-23"}, {"credit_no": "911400007671274376", "reg_no": "140000400016442", "oper_name": "宗庆后", "name": "山西娃哈哈食品有限公司", "id": "ea19198d-9d31-481f-b0ea-76acf814bcdb", "start_date": "2004-11-23"}, {"credit_no": "9154000068680765XP", "reg_no": "540000400000079", "oper_name": "宗庆后", "name": "西藏娃哈哈食品有限公司", "id": "573f160f-4698-4266-a78a-e4c8e2959790", "start_date": "2009-09-25"}, {"credit_no": "91340100758532713D", "reg_no": "341400400001816", "oper_name": "宗庆后", "name": "巢湖娃哈哈食品有限公司", "id": "9edc1c04-1dd4-43dd-a21a-22421b309f4e", "start_date": "2004-03-15"}, {"credit_no": "914211007510065692", "reg_no": "421100400000245", "oper_name": "徐浩", "name": "红安娃哈哈食品有限公司", "id": "ad0eb418-24f6-4bd8-838c-f24974b09cff", "start_date": "2003-06-17"}, {"credit_no": "915201007801681029", "reg_no": "520100400019160", "oper_name": "宗庆后", "name": "贵阳娃哈哈食品有限公司", "id": "8a4baafc-3f3e-4b55-8385-ad532573ea19", "start_date": "2005-11-28"}, {"credit_no": "91532900745268845X", "reg_no": "532900400000163", "oper_name": "龚金平", "name": "大理娃哈哈食品有限公司", "id": "d25e6e48-2c62-407c-807d-c0901de7d386", "start_date": "2003-01-20"}, {"credit_no": "91210100798454123W", "reg_no": "210100400002435", "oper_name": "宗庆后", "name": "沈阳娃哈哈荣泰食品有限公司", "id": "de9d4cc0-6e02-4e54-abb3-1dbb4d3cf61c", "start_date": "2007-02-28"}, {"credit_no": "91330101673957579W", "reg_no": "330198000005743", "oper_name": "宗庆后", "name": "杭州娃哈哈启力食品集团有限公司", "id": "e9c88f76-253a-4a12-b8d8-f8df600d3fba", "start_date": "2008-03-31"}]}}
    data6 = """{"credit_no": "91330100609136098C", "reg_no": "330100000109245", "oper_name": "宗庆后", "name": "杭州娃哈哈食品有限公司", "id": "b6d98c2a-9252-4a11-b230-c32955276ea3", "start_date": "1992-10-28"}"""
    data6_1 = """{"credit_no": "91330100609136098C"}"""
    path6_1 = ["data", "items", 0]

    result1 = {"code": "1000", "data": {"order_list": [{"order_id": "15879668630180002", "order_no": "15879668630180002", "serial_no": "", "order_name": "定制名称", "customize_info": "定制需求", "customize_type": "3", "requirement_file_name": "订单数据列表_20190628100949.xls", "requirement_file_url": "订单数据列表_20190628100949_1582610728960170000.xls", "collaboration_type": "", "collaboration_version": "", "order_type": "1", "payment_type": "", "order_from": "", "is_customize": "1", "custom_goods_id": "15826068170160000", "buyer_id": "15730961430270000", "buyer_name": "user951067", "buyer_real_name": "happy01", "buyer_mobile": "15982210001", "buyer_corp_id": "182818747638087680", "org_json": "", "buyer_org_id": "7011822724667952339", "buyer_org_name": "16CRM档案客户名称", "buyer_ip": "", "buyer_message": "", "buyer_invoice": "", "shop_id": "", "shop_name": "", "service_org_id": "-7422902346933186598", "service_org_name": "HAPPY单位", "goods_money": "", "order_money": "", "point": "", "point_money": "", "coupon_money": "", "coupon_id": "", "user_money": "", "user_platform_money": "", "promotion_money": "", "pay_money": "", "order_status": "1", "order_progress": "0", "pay_status": "", "review_status": "0", "feedback_status": "", "pay_time": "", "create_time": "2020-04-27 13:54:24", "finish_time": "", "is_deleted": "0", "tuangou_group_id": "", "agency_org_id": "-2763071546069595220", "agency_org_name": "21开发环境商家", "committer_id": "", "vip_commit_flag": "0", "industry": "IT服务（系统/数据/维护）", "buyer_head_img": "https://test-pic-2-bucket.obs.cn-north-1.myhuaweicloud.com:443/avatar419040880_1586698958955170000.png", "order_approval": "0", "order_open": "0", "order_source": "1", "order_committer_name": "", "order_committer_phone": "", "order_committer_date": "", "progress_list": [{"progress_id": 0, "progress_text": "需求沟通", "progress_time": "2020-04-27 13:54:24", "progress_status": 1}, {"progress_id": 1, "progress_text": "应用制作", "progress_time": "", "progress_status": 0}, {"progress_id": 2, "progress_text": "试用安装", "progress_time": "", "progress_status": 0}, {"progress_id": 3, "progress_text": "应用认证", "progress_time": "", "progress_status": 0}], "goods_list": [{"order_goods_id": "15879668640180000", "order_id": "15879668630180002", "is_customize": "1", "goods_package_source": "", "goods_package_source_name": "定制服务", "goods_id": "15826068170160000", "goods_name": "商品-20200225", "price": "", "num": "", "goods_money": "", "goods_picture": "https://test-pic-2-bucket.obs.cn-north-1.myhuaweicloud.com:443/图2_1573521199093170000.png", "goods_sn": "", "shop_id": "", "shop_name": "", "service_org_id": "-7422902346933186598", "service_org_name": "HAPPY单位", "goods_type": "", "goods_type_name": "", "buyer_id": "15730961430270000", "buyer_name": "user951067", "buyer_real_name": "happy01", "buyer_mobile": "15982210001", "buyer_corp_id": "182818747638087680", "service_code": "", "buyer_org_id": "7011822724667952339", "buyer_org_name": "16CRM档案客户名称", "charging_mode": "1", "charging_frequency": "0", "charging_duration": "0", "duration_unit": "0", "goods_package_trial_url": "", "goods_package_url": "", "goods_package_mplus_url": "", "goods_certificate_url": "", "goods_package_certificate_url": "", "goods_handbook_url": "", "form_total": "", "certificate_json": "", "certificate_status": "0", "certificate_time": "", "certificate_hash": "", "mplus_time": "", "mplus_hash": "", "goods_limit": "", "goods_expire_date": "", "supply_org_id": "-7422902346933186598", "supply_org_name": "", "goods_start_date": "", "sign_id": "", "certificate_id": "", "goods_app_version": "", "goods_app_id": "", "package_size": "", "transfer_status": "0", "design_plan": "", "supply_designer_id": "", "custom_goods_type": "", "custom_case_desc": "", "max_form_number": "", "return_type": "0", "return_status": "0", "old_exchange_id": "0", "license_update_time": "", "purchase_register_price": "0.00", "default_register_num": "0", "purchase_people_num": "0", "purchase_date_num": "0", "duration_num": "0", "frequency_num": "0", "choose_platform": "", "designer_name": "", "designer_qq": "", "designer_head_img": "", "designer_qq_url": ""}]}], "total_count": 1, "page_count": 20}, "message": "success"}
    path1 = [["data","order_list",0,"progress_list",0,"progress_time"]]
    # path1 = [["data", "order_list", 0, "progress_list", 0]]
    # path1 = [["data","order_list",0,"progress_list",0],["data","order_list",0,"progress_list"]]

    value1 = ["2020-04-27 13:54:24"]
    # value1 = """{"progress_id": 0, "progress_text": "需求沟通", "progress_time": "2020-04-27 13:54:24", "progress_status": 1}"""
    # value1 = """[{"progress_id": 0, "progress_text": "需求沟通", "progress_time": "2020-04-27 13:54:24", "progress_status": 1}, {"progress_id": 1, "progress_text": "应用制作", "progress_time": "", "progress_status": 0}, {"progress_id": 2, "progress_text": "试用安装", "progress_time": "", "progress_status": 0}, {"progress_id": 3, "progress_text": "应用认证", "progress_time": "", "progress_status": 0}]"""
    # value1 = ["""{"progress_id": 0, "progress_text": "需求沟通", "progress_time": "2020-04-27 13:54:24", "progress_status": 1}""","""[{"progress_id": 0, "progress_text": "需求沟通", "progress_time": "2020-04-27 13:54:24", "progress_status": 1}, {"progress_id": 1, "progress_text": "应用制作", "progress_time": "", "progress_status": 0}, {"progress_id": 2, "progress_text": "试用安装", "progress_time": "", "progress_status": 0}, {"progress_id": 3, "progress_text": "应用认证", "progress_time": "", "progress_status": 0}]"""]

    json7 = {"code": 1000, "message": "success", "data": None}
    data7 = """{"code": 1000,  "data": null}"""

    json8 = {"code": "1000", "data": {"code": 0, "data": {"order_id": "15936804110160000", "order_no": "15936804110160000"}, "message": "订单创建成功"}, "message": "success"}
    data8 = """{"code": 0, "message": "订单创建成功","order_id": "***"}"""

    json9 = {"code": -2, "data": {"code": -1, "data": "", "message": "商品：0520-线下商品-非0元,未匹配到适配版本,请更换商品或联系平台管理员"}, "message1": "success"}
    data9 = """{"code": -1, "message": "商品：###,未匹配到适配版本,请更换商品或联系#,平台管理员","message1": "success"}"""

    result2 = {"code": 1000, "message": "success", "data": [{"id": 15857072120160000, "permission_name": "经销商帮助中心",
            "permission_mark": "agency-help", "permission_url": "", "pid": 15857069560160000, "permission_type": 3,
            "is_permission": 1, "child": []}, {"id": 15857073520160000, "permission_name": "供应商帮助中心",
            "permission_mark": "supply-help", "permission_url": "", "pid": 15857069560160000, "permission_type": 3,
            "is_permission": 1, "child": []}, {"id": 15857074040160000, "permission_name": "服务商帮助中心", "permission_mark": "service-help",
            "permission_url": "", "pid": 15857069560160000, "permission_type": 3, "is_permission": 1, "child": []}]}
    path2 = [["data",1,"child",2,"permission_mark"]]
    value2 = ["agency-help"]

    json_value = json9
    data = data9

    re_result = result2
    re_path = path2
    re_value = value2

    json_path(re_result,re_path,re_value)

    # json_check(json_value, data)
