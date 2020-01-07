# -*- coding: utf-8 -*-
"""
接口：解析json
创建人：魏奇
更新人：魏奇
更新时间：2019-12-18 18:16
描述：
"""

# 检查json中和值
sign = []
def json_check(json,k,v):
    # keys = json.keys()
    # print(keys)
    # print(type(keys))

    if isinstance(json,dict): # 判断是否是字典类型isinstance 返回True,false
        dictionary = dict(json)
        for key in dictionary:
            if key == k:
                if dictionary[key] == v:
                    # print("key为%s,值为%s" % (key,dictionary[key]))
                    # print(True)
                    sign.append(True)
                    # return True,key,dictionary[key]
                else:
                    sign.append(False)
                    # return False,key,dictionary[key]
            elif isinstance(dictionary[key],dict):
                json_check(dictionary[key],k,v)

    # print(sgin)
    if sign and False not in sign:
        return True
    else:
        return False




if __name__ == "__main__":
    import json
    json1 = {
        'code': 1000,
        'data': {
            'uid': '15634425470190000',
            'mobile': '15982286537',
            'token': {
                'access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjaG9tZSIsImlhdCI6MTU3NjY2MzU5Nywic2NvcGVzIjoicm9sZV9hY2Nlc3MiLCJleHAiOjE1NzkyNTU1OTcsInVpZCI6IjE1NjM0NDI1NDcwMTkwMDAwIn0.5aKSmTyB-riy-RqbSarWfPBlGMqqwfinO1mN1TtF81o', 'refresh_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjaG9tZSIsImlhdCI6MTU3NjY2MzU5Nywic2NvcGVzIjoicm9sZV9yZWZyZXNoIiwiZXhwIjoxNTc5MzQxOTk3LCJ1aWQiOiIxNTYzNDQyNTQ3MDE5MDAwMCJ9.ZIaHM2boqnuwvuRf4TW2vq08jBltQVzNnjWb1xeJrNI',
                'token_type': 'bearer',
                'uid': '15634425470190000'
            }
        },
        'message': '',
        "uid": "15634425470190000"
        # 'mobile': '15982286537'
    }

    data = """{"mobile": "15982286537","uid": "15634425470190000"
            }"""
    print(type(data))
    Except = json.loads(data)
    si = []
    for key in Except.keys():
        check = json_check(json1,key,Except[key])
        # print(check)
        if check == True:
            print("检查成功。key为%s，值为%s" % (key,Except[key]))
        else:
            print("检查失败。key为%s，值为%s" % (key,Except[key]))




