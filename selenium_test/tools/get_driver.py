

from selenium import webdriver


class GetDriver:   #1.申明driver变量
    __web_driver=None
    @classmethod
    def get_web_driver(cls,url):
        if cls.__web_driver is None:
             #设置driver操作:1.获取浏览器;2.最大化浏览器;3.打开url
            cls.__web_driver = webdriver.Edge()  #后续可用selenium_grid 多线程
            cls.__web_driver.maximize_window()
            cls.__web_driver.get(url)
        return cls.__web_driver
    @classmethod
    def quit_web_driver(cls):    #退出driver方法
        if cls.__web_driver:
            cls.__web_driver.quit()   #driver退出,但是__web_driver仍存在内存地址
            cls.__web_driver=None     #__web_driver置空操作