from time import sleep

from selenium.webdriver.common.by import By

from base.base import Base
class WebBase(Base):
    """以下为 web专属方法"""
    def web_base_click_element(self,placeholder_text,click_text):
        loc=By.CSS_SELECTOR,"[placehold=请选择]"   #1.点击复选框
        self.base_chilk(loc)
        sleep(1)
        loc=By.XPATH,"//*[text()='{}']".format(placeholder_text)  #动态传参
        self.base_chilk(loc)    #点击复选框的内容


