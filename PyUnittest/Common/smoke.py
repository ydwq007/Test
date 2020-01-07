# -*- coding: utf-8 -*-
"""
接口：移动端登录接口- unittest
创建人：魏奇
更新人：魏奇
更新时间：2019-08-08
"""
class Smoke():
    def __init__(self,parm=True):
        self.parm = parm

    def smoke(self):
        if self.parm == False:
            return  False
        else:
            return True


if __name__ == "__main__":
    Smoke()