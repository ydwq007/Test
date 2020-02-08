# -*- coding: utf-8 -*-
"""
接口：用例执行前后的操作
创建人：魏奇
更新人：魏奇
更新时间：2019-11-13 9:21
描述：
"""
import unittest

class Plan(unittest.TestCase): # 继承unittest.TestCase

    @classmethod
    def setUpClass(cls):
        #所有case执行之前的前置，测试用例需要登录web，可以先实例化浏览器
        print("\n","--------脚本执行开始---------","\n")

    @classmethod
    def tearDownClass(cls):
        #所有case执行之后的后置，如关闭数据库连接。关闭浏览器。
        print("\n","--------脚本执行完成---------","\n")

    def setUp(self):
        # # 每个测试用例执行之前做操作
        print("\n","--------用例执行开始---------","\n")

    def tearDown(self):
        # 每个测试用例执行之后做操作
        print("\n","--------用例执行完成---------","\n")