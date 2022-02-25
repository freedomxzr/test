#导包
import logging.handlers

import os

from config import BASE_PATH


class GetLog:#新建类
    __logger =None #新建日志器变量
    @classmethod
    def get_logger(cls):  #新建获取日志器的方法
        """判断日志器是否为空,若为空:
        1.获取日志器
        2.修改默认级别
        3.获取处理器
        4.获取格式器
        5.将格式器添加到处理器中
        6.将处理器添加到日志器中
        """
        if cls.__logger is None:
            cls.__logger= logging.getLogger()
            cls.__logger.setLevel(logging.INFO)  # info记录步骤,error记录错误信息
            log_path=BASE_PATH +os.sep+"log"+os.sep+"xm1.log"
            th =logging.handlers.TimedRotatingFileHandler(filename=log_path,
                                                          when="midnight",  #一天一夜
                                                          interval=1,       #间隔1
                                                          backupCount=3,    #备份数量3
                                                          encoding='utf-8')
            fmt="%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            fm=logging.Formatter(fmt)
            th.setFormatter(fm)                #5.将格式器添加到处理器中
            cls.__logger.addHandler(th)        #6.将处理器添加到日志器中
        return cls.__logger
if __name__ == '__main__':
    log=GetLog.get_logger()
    print(type(log))
    log.info("test信息级别")
    log.error('test错误级别')