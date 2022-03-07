import os
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from config import BASE_PATH
from tools.get_log import GetLog

log=GetLog.get_logger()
class Base:    #page页面基类,page页面的公共方法
    def __init__(self,driver):#初始化操作,获取driver
        '''
        解决driver问题
        '''
        log.info("正在初始化driver:{}".format(driver))
        self.driver=driver
    def base_find(self, loc,timeout=30,poll_frequence=0.5):#查找 元素方法封装
        """
        显示等待:1.返回元素 2.x就是self.driver(until方法)
        :param loc:格式为列表或者元组,内容:元素定位信息使用By类
        :param timeout:查找元素超时时间,默认30秒
        :param poll_frequence:查找元素频率,默认0.5秒
        """
        log.info("正在查找元素".format(loc))
        return (WebDriverWait(self.driver,
                              timeout=timeout,
                              poll_frequency=poll_frequence).until(lambda x:x.find_element(loc[0],loc[1])))

    def base_input(self,loc,value):#输入 方法封装
        """
        操作顺序:1.获取元素 2.清空操作 3.输入操作
        :param loc:元素定位信息
        :param value:输入内容
        """
        el=self.base_find(loc)
        log.info("正在对{}元素进行清空操作".format(loc))
        el.clear()
        log.info("正在对{}元素进行输入操作{}".format(loc,value))
        el.send_keys(value)
    def base_chilk(self,loc):#点击 方法封装
        """"
        :param loc: 元素定位信息
        """
        self.base_find(loc).click()
    def base_get_text(self, loc):#获取 元素文本方法封装
        """"
        :param loc: 元素定位信息
        :return: 放回元素文本值
        """
        log.info("正在对{}元素进行获取文本,获取的文本为{}".format(loc,self.base_find(loc).text))
        return self.base_find(loc).text
    def base_get_img(self,page_name="xmglht"):#截图方法封装，用户断言失败时候调用
        path = BASE_PATH + os.sep + "image" + os.sep + page_name
        if not os.path.exists(path):
            os.makedirs(path)
        log.info("正在截取{}页面图片".format(page_name))
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        try:
            print(path)
            filename=path+os.sep+page_name+picture_time+'.png'
            picture_url=self.driver.get_screenshot_as_file(filename)
            log.info("截图成功,文件为:{}".format(filename))
        except BaseException as e:
            print(e)
