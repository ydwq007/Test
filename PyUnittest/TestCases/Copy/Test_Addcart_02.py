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
sys.path.append('../../Interfaces') #跨目录调用需要配置路径,接口路径
import Logins.Login as Login
import Searchs.SearchGoods as SearchGoods
import Goods.AddCart as AddCart
import Goods.GetCartList as GetCartList

url = test_url_chome
class Add_cart(unittest.TestCase): # 继承unittest.TestCase
# class add_cart():

    #登录操作
    def test_01(self):
        """登录操作的情况"""
        self.user =  usernames[0] #用户名
        self.passw = password #密码
        self.goods = "商品升级-普通版"

        #登录
        try:
            self.result_login = Login.login_mobile(url,self.user, self.passw, "") #获取接口成功或失败的标记
            self.assertEqual(True,self.result_login[0])
        except TypeError:
            print("验证码次数超过最多限制,SendCode接口报错")
        except IndexError:
            print("序列中没有此索引(index),SendCode接口报错")
        finally:
            print("已调用登录接口")

        #查询商品
        try:
            self.result_search = SearchGoods.goods_search(self.goods) #获取接口成功或失败的标记
            self.assertEqual(True, self.result_search[0])
        finally:
            print("已调用搜索商品接口")

        #查看购物车
            try:
                self.result_showcart = GetCartList.getcartlist(self.result_login[2], self.result_login[3]) #获取接口成功或失败的标记
                self.assertEqual(True, self.result_showcart[0])
            finally:
                print("已调用查看购物车接口")


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



if __name__ == '__main__':
    unittest.main()
    # add_cart()