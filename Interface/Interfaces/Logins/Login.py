# -*- coding: utf-8 -*-
#登录接口
#y由于PC端是PHP渲染，通过表单提交，但是无法做登录接口测试，故采取移动端的登录接口
import requests,json,re,logging,csv,sys
sys.path.append(r'D:\IdeaProjects\seeyon\Interface\TestDatas') #跨目录调用需要配置路径
from bson import json_util
import SendCode
from BasicDatas import mobile,parameter_login,test_chome,headers
# # logging.basicConfig(level=logging.DEBUG)

#基本参数：
#登录接口地址
login_url = "%s/portal.php" % test_chome
#选择登录方式
Login_mode = 1 #1代表密码登录，否则代表验证码登录

#封装登录接口
def re_login():

    #设置接口参数
    if Login_mode == 1:
        #密码登录
        login_data1 = {
            "m":"userMobileLogin",
            "a":"login",
            "username":username,
            "password":password,
            "account_type":"1" #1: A类（商城）  2: B类（云工厂）
        }
        login_datas = json.dumps(login_data1) #json.dumps()用于将字典形式的数据转化为json字符串
    else:
        #验证码登录
        SendCode.sendcode(mobile) #参数为电话号码，验证码类型（可不传，默认为登录），验证码方式（可不传，默认为手机）
        randcode = SendCode.sendcode(mobile) #将获取到的验证码赋值给randcode，返回的是一个列表
        login_data2 = {
            "m":"userMobileLogin",
            "a":"loginByCode",
            "mobile":mobile,
            "randcode":randcode[0]
        }
        login_datas = json.dumps(login_data2) ##json.dumps()用于将字典形式的数据转化为json字符串

    #调用请求
    request_login = requests.post(login_url, data=login_datas,headers=headers,verify=False) #调用接口（url,参数，类型）#verify=False 跳过认证
    #获取响应数据
    response_login= json.loads(request_login.text) #son.loads()用于将字符串形式的数据转化为字典

    #调试时打印
    # print("-----------打印请求数据如下：--------------")
    # print(login_url)
    # print(login_datas)
    # print(json_util.dumps(data,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出

    print("---------打印响应结果：---------------")
    # print(json_util.dumps(response_login,ensure_ascii=False,indent=4)) #打印请求数据，以json格式输出
    # if "uid" in response_login["data"].keys(): #通过字段判断
    if response_login["code"] == 1000: #通过响应码判断
        #分解成功情况
        token = response_login["data"]["token"]["access_token"]
        if Login_mode == 1:
            print("username为%s的用户登录成功！！！token为：%s" % (username,token))
        else:
            print("mobile为%s的用户登录成功！！！token为：%s" % (mobile,token))
        return True
    else:
        #分解失败情况
        message = response_login["message"]
        if Login_mode == 1:
            if username == "":
                print("username为空的用户登录失败！！！原因为：%s" % message)
            else:
                print("username为%s的用户登录失败！！！原因为：%s" % (username,message))
        else:
            print("mobile为%s的用户登录失败！！！原因为：%s" % (mobile,message))
        return False

if __name__ == "__main__":
    n = 1 #统计执行总次数
    pass_count = 0 #成功次数
    fail_count = 0 #失败次数
    for i in parameter_login:
        print("第%s次执行案例，案例内容：%s" % (n,i[0]))
        username = i[1]
        password = i[2]
        n += 1
        #异常处理try
        try:
            re_login() #调用接口
            result = re_login() #获取接口成功会失败的标记
            #统计案例执行情况
            # if assertEqual(i[3], result):
            #     pass_count += 1
            # else:
            #     fail_count += 1

            if result == i[3]:
                pass_count += 1
            else:
                fail_count += 1
        except TypeError:
            print("验证码次数超过最多限制,SendCode接口报错")
        except IndexError:
            print("序列中没有此索引(index),SendCode接口报错")
        finally:
            print("已调用接口")

    #打印案例执行情况，方便统计
    print("----------案例执行结果如下：-------------")
    print("执行通过%s案例，执行失败%s案例，案例通过率：%.2f%%" %(pass_count,fail_count,pass_count/(n-1)*100))
    print("执行通过%s案例，执行失败%s案例，案例通过率：%.2f%%" %(pass_count,fail_count,pass_count/(pass_count+fail_count)*100))
