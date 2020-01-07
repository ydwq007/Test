# -*- coding: utf-8 -*-
"""
接口：
创建人：魏奇
创建时间：
更新时间：
描述：
"""
import unittest,sys
sys.path.append('../../TestDatas') #跨目录调用需要配置路径，测试数据路径
from BasicDatas import usernames,password
sys.path.append('../../Interfaces') #跨目录调用需要配置路径,接口路径
import Logins.Login as Login
import FormVote.Form_Creat as Form_Creat


class Form_Creat_Cases(unittest.TestCase): # 继承unittest.TestCase

    @classmethod
    def setUpClass(cls):
        #所有case执行之前的前置，测试用例需要登录web，可以先实例化浏览器
        print("\n","------脚本执行开始-------","\n",)

    @classmethod
    def tearDownClass(cls):
        #所有case执行之后的后置，如关闭数据库连接。关闭浏览器。
        print("\n","--------脚本执行结束-------","\n")

    def setUp(self):
        # 每个测试用例执行之前做操作
        print("\n","------案例开始执行-------","\n")
        self.user = usernames[0]
        self.passw = password
        self.realname = "接口测试表单上传" #真实姓名
        self.org_name = "接口测试数据-表单上传" #单位名称
        self.mobile = "15982280808" #电话号码
        self.goods_file = "表单名称_1568253714868170000.sfp" #表单文件
        self.img_url = "https://test-pic-2-bucket.obs.cn-north-1.myhuaweicloud.com:443/" \
                       "%E5%8A%A8%E5%9B%BE_1568253738587170000.gif" #表单图片
        self.domain = "人事管理" #领域
        self.desc1 = "接口测试表单001" #描述
        self.desc2 = "接口测试套表001" #描述


    def tearDown(self):
        # 每个测试用例执行之后做操作
        print("\n","------案例完成执行------","\n")

    def test_01(self):
        """上传表单--正常数据"""
        #参数
        self.data = {
            "realname": self.realname, #真实姓名
            "org_name": self.org_name, #单位名称
            "mobile": self.mobile, #电话号码
            "type": 1, #上传类型，1表单，2套表
            #表单列表
            "form_list": [{
                "goods_file": self.goods_file, #表单文件
                "img_url": self.img_url, #表单图片
                "domain": self.domain, #领域
                "desc": self.desc1 #描述
            },
                {
                    "goods_file": "表单名称_1568253714868170000.sfp", #表单文件
                    "img_url": "https://test-pic-2-bucket.obs.cn-north-1.myhuaweicloud.com:443"
                               "/%E5%8A%A8%E5%9B%BE_1568253738587170000.gif", #表单图片
                    "domain": "人事管理", #领域
                    "desc": "接口测试表单002" #描述
                }]
        }
        #调用登录接口
        self.result_login = Login.login_mobile(self.user, self.passw, "") #获取接口成功会失败的标记

        #调用上传表单接口
        try:
            self.result_uploadform = Form_Creat.uploadform(self.result_login[3], self.data) #获取接口成功会失败的标记
            self.assertEqual(True, self.result_uploadform)
        finally:
            print("已调用上传表单接口")

    def test_02(self):
        """上传套表--正常数据"""
        #参数
        self.data = {
            "realname": self.realname, #真实姓名
            "org_name": self.org_name, #单位名称
            "mobile": self.mobile, #电话号码
            "type": 2, #上传类型，1表单，2套表
            #表单列表
            "form_list": [{
                "goods_file": self.goods_file, #表单文件
                "img_url": self.img_url, #表单图片
                "form_name":"测试套表数据", #表单名称type=2 必填
                "domain": self.domain, #领域
                "desc": self.desc2 #描述
            },
                {
                    "goods_file": "表单名称_1568253714868170000.sfp", #表单文件
                    "img_url": "https://test-pic-2-bucket.obs.cn-north-1.myhuaweicloud.com:443"
                               "/%E5%8A%A8%E5%9B%BE_1568253738587170000.gif", #表单图片
                    "form_name":"测试套表数据", #表单名称type=2 必填
                    "domain": "人事管理", #领域
                    "desc": "接口测试套表002" #描述
                }]
        }
        #调用登录接口
        self.result_login = Login.login_mobile(self.user, self.passw, "") #获取接口成功会失败的标记

        #调用上传表单接口
        try:
            self.result_uploadform = Form_Creat.uploadform(self.result_login[3], self.data) #获取接口成功会失败的标记
            self.assertEqual(True, self.result_uploadform)
        finally:
            print("已调用上传表单接口")

    def test_03(self):
        """上传表单--未登录"""
        self.token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjaG9tZSIsImlhdCI6MTU2NjQzNjg0Miwi" \
                     "c2NvcGVzIjoicm9sZV9hY2Nlc3MiLCJleHAiOjE1NjkwMjg4NDIsInVpZCI6IjE1NjI2NTAzNzUwMTkwMDAwIn0.Gl7" \
                     "7PNZsgSFF1nU4CF0HxJLcqjevUHxdPx50TUqXRCc1" #登录token
        #参数
        self.data = {
            "realname": self.realname, #真实姓名
            "org_name": self.org_name, #单位名称
            "mobile": self.mobile, #电话号码
            "type": 1, #上传类型，1表单，2套表
            #表单列表
            "form_list": [{
                "goods_file": self.goods_file, #表单文件
                "img_url": self.img_url, #表单图片
                "domain": self.domain, #领域
                "desc": self.desc1 #描述
            }]
        }

        #调用上传表单接口
        try:
            self.result_uploadform = Form_Creat.uploadform(self.token, self.data) #获取接口成功会失败的标记
            self.assertEqual(False, self.result_uploadform)
        except Exception as err:
            raise err
        finally:
            print("已调用上传表单接口")

    def test_04(self):
        """上传表单--真实姓名未填写"""
        #调用登录接口
        self.result_login = Login.login_mobile(self.user, self.passw, "") #获取接口成功会失败的标记
        #参数
        self.data = {
            "realname": "", #真实姓名
            "org_name": self.org_name, #单位名称
            "mobile": self.mobile, #电话号码
            "type": 1, #上传类型，1表单，2套表
            #表单列表
            "form_list": [{
                "goods_file": self.goods_file, #表单文件
                "img_url": self.img_url, #表单图片
                "domain": self.domain, #领域
                "desc": self.desc1 #描述
            }]
        }
        #调用上传表单接口
        try:
            self.result_uploadform = Form_Creat.uploadform(self.result_login[3], self.data) #获取接口成功会失败的标记
            self.assertEqual(False, self.result_uploadform)
        except Exception as err:
            raise err
        finally:
            print("已调用上传表单接口")

    def test_05(self):
        """上传表单--单位名称未填写"""
        #调用登录接口
        self.result_login = Login.login_mobile(self.user, self.passw, "") #获取接口成功会失败的标记
        #参数
        self.data = {
            "realname": self.realname, #真实姓名
            "org_name": "", #单位名称
            "mobile": self.mobile, #电话号码
            "type": 1, #上传类型，1表单，2套表
            #表单列表
            "form_list": [{
                "goods_file": self.goods_file, #表单文件
                "img_url": self.img_url, #表单图片
                "domain": self.domain, #领域
                "desc": self.desc1 #描述
            }]
        }
        #调用上传表单接口
        try:
            self.result_uploadform = Form_Creat.uploadform(self.result_login[3], self.data) #获取接口成功会失败的标记
            self.assertEqual(False, self.result_uploadform)
        except Exception as err:
            raise err
        finally:
            print("已调用上传表单接口")

    def test_06(self):
        """上传表单--电话号码未填写"""
        #调用登录接口
        self.result_login = Login.login_mobile(self.user, self.passw, "") #获取接口成功会失败的标记
        #参数
        self.data = {
            "realname": self.realname, #真实姓名
            "org_name": self.org_name, #单位名称
            "mobile": "", #电话号码
            "type": 1, #上传类型，1表单，2套表
            #表单列表
            "form_list": [{
                "goods_file": self.goods_file, #表单文件
                "img_url": self.img_url, #表单图片
                "domain": self.domain, #领域
                "desc": self.desc1 #描述
            }]
        }
        #调用上传表单接口
        try:
            self.result_uploadform = Form_Creat.uploadform(self.result_login[3], self.data) #获取接口成功会失败的标记
            self.assertEqual(False, self.result_uploadform)
        except Exception as err:
            raise err
        finally:
            print("已调用上传表单接口")

    def test_07(self):
        """上传表单--表单文件未填写"""
        #调用登录接口
        self.result_login = Login.login_mobile(self.user, self.passw, "") #获取接口成功会失败的标记
        #参数
        self.data = {
            "realname": self.realname, #真实姓名
            "org_name": self.org_name, #单位名称
            "mobile": self.mobile, #电话号码
            "type": 1, #上传类型，1表单，2套表
            #表单列表
            "form_list": [{
                "goods_file": "", #表单文件
                "img_url": self.img_url, #表单图片
                "domain": self.domain, #领域
                "desc": self.desc1 #描述
            }]
        }
        #调用上传表单接口
        try:
            self.result_uploadform = Form_Creat.uploadform(self.result_login[3], self.data) #获取接口成功会失败的标记
            self.assertEqual(False, self.result_uploadform)
        except Exception as err:
            raise err
        finally:
            print("已调用上传表单接口")

    def test_08(self):
        """上传表单--表单图片未填写"""
        #调用登录接口
        self.result_login = Login.login_mobile(self.user, self.passw, "") #获取接口成功会失败的标记
        #参数
        self.data = {
            "realname": self.realname, #真实姓名
            "org_name": self.org_name, #单位名称
            "mobile": self.mobile, #电话号码
            "type": 1, #上传类型，1表单，2套表
            #表单列表
            "form_list": [{
                "goods_file": self.goods_file, #表单文件
                "img_url": "", #表单图片
                "domain": self.domain, #领域
                "desc": self.desc1 #描述
            }]
        }
        #调用上传表单接口
        try:
            self.result_uploadform = Form_Creat.uploadform(self.result_login[3], self.data) #获取接口成功会失败的标记
            self.assertEqual(False, self.result_uploadform)
        except Exception as err:
            raise err
        finally:
            print("已调用上传表单接口")

    def test_09(self):
        """上传表单--领域未填写"""
        #调用登录接口
        self.result_login = Login.login_mobile(self.user, self.passw, "") #获取接口成功会失败的标记
        #参数
        self.data = {
            "realname": self.realname, #真实姓名
            "org_name": self.org_name, #单位名称
            "mobile": self.mobile, #电话号码
            "type": 1, #上传类型，1表单，2套表
            #表单列表
            "form_list": [{
                "goods_file": self.goods_file, #表单文件
                "img_url": self.img_url, #表单图片
                "domain": "", #领域
                "desc": self.desc1 #描述
            }]
        }
        #调用上传表单接口
        try:
            self.result_uploadform = Form_Creat.uploadform(self.result_login[3], self.data) #获取接口成功会失败的标记
            self.assertEqual(False, self.result_uploadform)
        except Exception as err:
            raise err
        finally:
            print("已调用上传表单接口")

    def test_10(self):
        """上传表单--描述未填写"""
        #调用登录接口
        self.result_login = Login.login_mobile(self.user, self.passw, "") #获取接口成功会失败的标记
        #参数
        self.data = {
            "realname": self.realname, #真实姓名
            "org_name": self.org_name, #单位名称
            "mobile": self.mobile, #电话号码
            "type": 1, #上传类型，1表单，2套表
            #表单列表
            "form_list": [{
                "goods_file": self.goods_file, #表单文件
                "img_url": self.img_url, #表单图片
                "domain": self.domain, #领域
                "desc": "" #描述
            }]
        }
        #调用上传表单接口
        try:
            self.result_uploadform = Form_Creat.uploadform(self.result_login[3], self.data) #获取接口成功会失败的标记
            self.assertEqual(False, self.result_uploadform)
        except Exception as err:
            raise err
        finally:
            print("已调用上传表单接口")

    def test_11(self):
        """上传表单--未在时间范围内"""
        #参数
        self.data = {
            "realname": self.realname, #真实姓名
            "org_name": self.org_name, #单位名称
            "mobile": self.mobile, #电话号码
            "type": 1, #上传类型，1表单，2套表
            #表单列表
            "form_list": [{
                "goods_file": self.goods_file, #表单文件
                "img_url": self.img_url, #表单图片
                "domain": self.domain, #领域
                "desc": self.desc1 #描述
            },
                {
                    "goods_file": "表单名称_1568253714868170000.sfp", #表单文件
                    "img_url": "https://test-pic-2-bucket.obs.cn-north-1.myhuaweicloud.com:443"
                               "/%E5%8A%A8%E5%9B%BE_1568253738587170000.gif", #表单图片
                    "domain": "人事管理", #领域
                    "desc": "接口测试表单002" #描述
                }]
        }
        #调用登录接口
        self.result_login = Login.login_mobile(self.user, self.passw, "") #获取接口成功会失败的标记

        #调用上传表单接口
        try:
            self.result_uploadform = Form_Creat.uploadform(self.result_login[3], self.data) #获取接口成功会失败的标记
            self.assertEqual(False, self.result_uploadform)
        finally:
            print("已调用上传表单接口")


if __name__ == '__main__':
    unittest.main()