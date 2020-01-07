# -*- coding: utf-8 -*-
"""
接口：移动端登录接口 - 一般写法
创建人：魏奇
更新人：魏奇
更新时间：2019-07-11
"""
import unittest
import sys
sys.path.append('../../TestDatas') #跨目录调用需要配置路径，测试数据路径
from BasicDatas import parameter_login

sys.path.append('../../Interfaces') #跨目录调用需要配置路径,接口路径
import Logins.Login as Login


class Login_cases(unittest.TestCase): # 继承unittest.TestCase

    def test_results(self):
        n = 1 #统计执行总次数
        pass_count = 0 #成功次数
        fail_count = 0 #失败次数
        for i in parameter_login:
            print("\n""第%s次执行案例，案例内容：%s" % (n,i[0]))
            username = i[1]
            password = i[2]
            n += 1
            #异常处理try
            try:
                result = Login.login_mobile(username, password) #获取接口成功会失败的标记
                #统计案例执行情况
                #如果用断言判断执行情况，需要添加断言失败的异常，并且将失败的断言进行统计
                print(self.assertEqual(i[3], result[0]))
                if self.assertEqual(i[3], result[0]) == None:
                    pass_count += 1

            except Exception as err:
                print("第%s条案例断言失败，失败原因：%s" % ((n-1),err))
                fail_count += 1
            finally:
                print("已调用接口")

        #打印案例执行情况，方便统计
        print("----------案例执行结果如下：-------------")
        print("总共执行%s条案例，执行通过%s案例，执行失败%s案例，案例通过率：%.2f%%" % (n-1,pass_count,fail_count,pass_count/(n-1)*100))

if __name__ == '__main__':
    unittest.main()