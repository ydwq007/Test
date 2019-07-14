# -*- coding: utf-8 -*-
#登录接口
#y由于PC端是PHP渲染，通过表单提交，但是无法做登录接口测试，故采取移动端的登录接口
import requests,json,re,logging,csv,sys
sys.path.append(r'D:\IdeaProjects\seeyon\PyUnittest\TestDatas') #跨目录调用需要配置路径，测试数据路径
from BasicDatas import mobile,parameter_login,test_chome,headers
sys.path.append(r'D:\IdeaProjects\seeyon\PyUnittest\Interfaces\Logins') #跨目录调用需要配置路径,接口路径
import Login1
# # logging.basicConfig(level=logging.DEBUG)

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
        result = Login1.re_login(username,password,"") #获取接口成功会失败的标记
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
# print("执行通过%s案例，执行失败%s案例，案例通过率：%.2f%%" %(pass_count,fail_count,pass_count/(n-1)*100))
print("执行通过%s案例，执行失败%s案例，案例通过率：%.2f%%" %(pass_count,fail_count,pass_count/(pass_count+fail_count)*100))