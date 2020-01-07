# -*- coding: utf-8 -*-
"""
接口：获取实例或用例名称
创建人：魏奇
创建时间：2019-08-29
更新时间：2019-08-29
"""

import inspect #导入标准库，以获取类或函数的参数的信息，源码，解析堆栈，对对象进行类型检查


# 得到当前类的实例方法名
# 也就是获得用例的名称
def get_function_name():
    #inspect.stack()返回的是一个列表
    function_name = inspect.stack()
    # print(function_name)
    # print(function_name[1])
    return function_name[1][3]

if __name__ == "__main__":
    get_function_name()
