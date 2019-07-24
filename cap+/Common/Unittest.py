# -*- coding: utf-8 -*-
#定义判断真假的断言
import unittest

class Unitest(unittest.TestCase):

    def test_results(self):
        a = 123
        b =1231
        try:
            # self.assertEqual(a,b,msg="失败原因：%s  不等于 %s" % (a,b))
            print(self.assertEqual(a,b,msg="失败原因：%s  不等于 %s" % (a,b)))
        except AssertionError:
            print("断言失败，失败原因：期望值%s  不等于 实际值%s" % (a,b))

if __name__ == '__main__':
    unittest.main()

# class Unitest1(object): # 继承unittest.TestCase
#
#
#     def __init__(self,exception,result):
#         self._exception = exception
#         self._result = result
#
#
# class Unitest2(Unitest1,unittest.TestCase): # 继承unittest.TestCase
#
#
#     def test_results(self):
#         self.assertEqual(self._exception,self._result,msg="失败原因：%s  不等于 %s" % (self._exception,self._result))
#
#
# if __name__ == '__main__':
#     a = Unitest2(1,2)
#     a.test_results()
#     # Unitest(123,321)
#     # Unitest(111,111)