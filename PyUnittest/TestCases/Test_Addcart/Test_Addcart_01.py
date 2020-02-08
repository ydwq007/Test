# -*- coding: utf-8 -*-
"""
接口：加入购物车
创建人：魏奇
更新人：魏奇
更新时间：2019-08-20
备注：包含登录-搜索-加入购物车-浏览购物车
"""

import unittest,sys
sys.path.append('../../TestDatas') #跨目录调用需要配置路径，测试数据路径
from config import usernames,password,test_url_chome
sys.path.append('.../../Interfaces') #跨目录调用需要配置路径,接口路径
import Logins.Login as Login
import Searchs.SearchGoods as SearchGoods
import Goods.AddCart as AddCart
import Goods.GetCartList as GetCartList
import Goods.CleanCart as CleanCart

url = test_url_chome
class Add_cart(unittest.TestCase): # 继承unittest.TestCase

    @classmethod
    def setUpClass(cls):
        #所有case执行之前的前置，测试用例需要登录web，可以先实例化浏览器
        print("\n","----------脚本执行开始---------","\n")

    @classmethod
    def tearDownClass(cls):
        #所有case执行之后的后置，如关闭数据库连接。关闭浏览器。
        print("\n","------------脚本执行结束---------","\n")

    def setUp(self):
        # # 每个测试用例执行之前做操作
        print("\n","---------案例开始执行----------","\n")

    def tearDown(self):
        # 每个测试用例执行之后做操作
        print("\n","---------案例完成执行---------","\n")

    #在登录的情况下进行购物车操作
    def test_01(self):
        """在登录的情况下进行购物车操作（登录-查看购物车-查询商品-加入购物车-查看购物车）"""
        self.user =  usernames[0] #用户名
        self.passw = password #密码
        self.goods = "商品升级-普通版"

        #登录
        try:
            self.result_login = Login.login_mobile(url,self.user, self.passw, "") #获取接口成功或失败的标记
            self.assertEqual(True,self.result_login[0])
        finally:
            print("已调用登录接口")

        #查询商品
        try:
            self.result_search = SearchGoods.goods_search(self.goods) #获取接口成功或失败的标记
            self.assertEqual(True, self.result_search[0])
        finally:
            print("已调用搜索商品接口")

        #商品加入购物车，保证购物车有数据
        try:
            self.result_cart = AddCart.addcart(self.result_login[2], self.result_search[1], self.result_login[3]) #获取接口成功或失败的标记
            self.assertEqual(True,self.result_cart)
        finally:
            print("已调用加入购物车接口")

        #清空购物车
        try:
            self.result_cleancart = CleanCart.cleancart(self.result_login[2], self.result_login[3]) #获取接口成功或失败的标记
            self.assertEqual(True, self.result_cleancart)
        finally:
            print("已调用清空购物车接口")

        #查看购物车是否被清空
        try:
            self.result_showcart = GetCartList.getcartlist(self.result_login[2], self.result_login[3]) #获取接口成功或失败的标记
            self.assertEqual(True,self.result_showcart[0])
        except UnboundLocalError:
            print("购物车为空")
        finally:
            print("已调用查看购物车接口")

        #查询商品
        try:
            self.result_search = SearchGoods.goods_search(self.goods) #获取接口成功或失败的标记
            self.assertEqual(True, self.result_search[0])
        finally:
            print("已调用搜索商品接口")

        #商品加入购物车
        try:
            self.result_cart = AddCart.addcart(self.result_login[2], self.result_search[1], self.result_login[3]) #获取接口成功或失败的标记
            self.assertEqual(True,self.result_cart)
        finally:
            print("已调用加入购物车接口")

        #查看购物车
        try:
            self.result_showcart = GetCartList.getcartlist(self.result_login[2], self.result_login[3]) #获取接口成功或失败的标记
            self.assertEqual(True, self.result_showcart[0])
        finally:
            print("已调用查看购物车接口")

    def test_02(self):
        """在未登录的情况下查看购物车操作（"""
        uid =  15626503750190000 #用户id
        token = "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjaG9tZSIsImlhdCI6MTU2NjQzNjg0Miwi" \
                     "c2NvcGVzIjoicm9sZV9hY2Nlc3MiLCJleHAiOjE1NjkwMjg4NDIsInVpZCI6IjE1NjI2NTAzNzUwMTkwMDAwIn0.Gl7" \
                     "7PNZsgSFF1nU4CF0HxJLcqjevUHxdPx50TUqXRCc1" #登录token

        #查看购物车
        try:
            self.result_showcart = GetCartList.getcartlist(uid, token) #获取接口成功或失败的标记
            self.assertEqual(False, self.result_showcart)
        finally:
            print("已调用查看购物车接口")

    def test_03(self):
        """在未登录的情况下添加商品进入购物车"""
        goods = "商品升级-普通版"
        uid =  15626503750190000 #用户id
        token = "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjaG9tZSIsImlhdCI6MTU2NjQzNjg0Miwi" \
                "c2NvcGVzIjoicm9sZV9hY2Nlc3MiLCJleHAiOjE1NjkwMjg4NDIsInVpZCI6IjE1NjI2NTAzNzUwMTkwMDAwIn0.Gl7" \
                "7PNZsgSFF1nU4CF0HxJLcqjevUHxdPx50TUqXRCc1" #登录token

        #查询商品
        try:
            self.result_search = SearchGoods.goods_search(goods) #获取接口成功或失败的标记
            self.assertEqual(True, self.result_search[0])
        finally:
            print("已调用搜索商品接口")

        #商品加入购物车
        try:
            self.result_cart = AddCart.addcart(uid, self.result_search[1], token) #获取接口成功或失败的标记
            self.assertEqual(False,self.result_cart)
        finally:
            print("已调用加入购物车接口")

    def test_04(self):
        """删除购物车中指定的商品（登录-加入购物车-查看购物车-删除购物车商品-查看购物车）"""
        user =  usernames[0] #用户名
        passw = password #密码

        #登录
        try:
            self.result_login = Login.login_mobile(url,user, passw, "") #获取接口成功或失败的标记
            self.assertEqual(True,self.result_login[0])
        # except AssertionError:
        #     print("断言失败，失败原因：期望值%s  不等于实际值 True" % self.result_login[0])
        except TypeError:
            print("验证码次数超过最多限制,SendCode接口报错")
        except IndexError:
            print("序列中没有此索引(index),SendCode接口报错")
        finally:
            print("已调用登录接口")

        #添加购物车
            try:
                self.result_cart = AddCart.addcart(self.result_login[2], "15711027370160000", self.result_login[3]) #获取接口成功或失败的标记
                self.assertEqual(True,self.result_cart)
            finally:
                print("已调用加入购物车接口")

        #查看购物车
        try:
            self.result_showcart = GetCartList.getcartlist(self.result_login[2], self.result_login[3]) #获取接口成功或失败的标记
            self.assertEqual(True,self.result_showcart[0])
            self.cart_id = list(self.result_showcart[2].values())
            print(self.cart_id )
        except UnboundLocalError:
            print("购物车为空")
        finally:
            print("已调用查看购物车接口")

        #删除购物车中指定的商品
        try:
            self.result_cleancart = CleanCart.cleancart(self.result_login[2], self.result_login[3], False, self.cart_id[0]) #获取接口成功或失败的标记
            self.assertEqual(True, self.result_cleancart)
        finally:
            print("已调用删除购物车商品接口")

        #查看购物车
        try:
            self.result_showcart = GetCartList.getcartlist(self.result_login[2], self.result_login[3]) #获取接口成功或失败的标记
            self.assertEqual(True,self.result_showcart[0])
        except UnboundLocalError:
            print("购物车为空")
        finally:
            print("已调用查看购物车接口")

if __name__ == '__main__':
    unittest.main()
    # add_cart()