# -*- coding: utf-8 -*-
"""
接口：执行日志
创建人：魏奇
更新人：魏奇
更新时间：2019-11-20 17:27
描述：
"""

import logging

def get_logger():
    global logPath
    try:
        logPath
    except NameError:
        logPath = ""
    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=FORMAT)
    return logging