# row = 5
# for i in range(row):
#     for _ in range(row - i - 1):
#         print(' ', end='')
#     for _ in range(2 * i + 1):
#         print('*', end='')
#     print()
#
#
# for i in range(row):
#     for j in range(row - i):
#         print(' ', end='')
#     for j in range(2 * i+1):
#         print('*', end='')
#     print()

# from random import randint
# i = True
# while i:
#     first = randint(1, 6) + randint(1, 6)
#     if first < 11:
#         print(first)
#     else:
#         i = False
#         print(first)
#         break

# a = 153
# print(a%10)
# print(a//10)
# print(a//100)



# def hws(n):
#     num1 = str(n)
#     num2 = num1[::-1]
#     print(num1)
#     print(num2)
#     if num1 == num2:
#         return True
#     else:
#         return False
# print(hws(121))

# import time
# import math
#
# start = time.process_time()
# for num in range(1, 10000):
#     sum = 0
#     for factor in range(1, int(math.sqrt(num)) + 1):
#         if num % factor == 0:
#             sum += factor
#             if factor > 1 and num / factor != factor:
#                 sum += num / factor
#     if sum == num:
#         print(num)
# end = time.process_time()
# print("执行时间:", (end - start), "秒")


# -*- coding: utf-8 -*-
# #定义判断真假的断言
# import unittest
#
# class Unitest(unittest.TestCase):
#
#     def test_results(self):
#         a = True
#         b = True
#         print(self.assertEqual(1,1))
#         # self.assertEqual(a,b,msg="失败原因：%s  不等于 %s" % (a,b))
#
# if __name__ == '__main__':
#     unittest.main()

import time
import datetime

startTime = datetime.datetime.now()
print(type(startTime))

topTime = datetime.datetime.now()
duration = topTime - startTime
print(duration)