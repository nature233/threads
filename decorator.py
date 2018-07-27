#! /usr/bin/env python3 
# -*- coding: utf-8 -*-

import traceback
import logging
from logging.handlers import TimedRotatingFileHandler
import functools

 #filename  可以设置log的位置和输出的名字
def loggerInFile(filename):#带参数的装饰器需要2层装饰器实现,第一层传参数，第二层传函数，每层函数在上一层返回
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs): #1
            logFilePath = filename  # 日志按日期滚动，保留5天
            logger = logging.getLogger()
            logger.setLevel(logging.NOTSET)
            handler = TimedRotatingFileHandler(logFilePath,
                                               when="d",
                                               interval=1,
                                               backupCount=5000)
            formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s-%(module)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            try:
                #print("Arguments were: %s, %s" % (args, kwargs))
                result = func(*args, **kwargs) #2
                #logger.info(result)
                #return result
                logger.info(' the function is %s'%func
                            +" Arguments were: %s, %s" % (args, kwargs) + "  the result of is  %s  "%result)
            except:
                logger.error(traceback.format_exc())
        return inner
    return decorator