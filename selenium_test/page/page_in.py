from page.page_xmglht_login import PageXmglhtLogin


class PageIn():  #统一入口类,统一管理!
    def __init__(self,driver):
        self.driver=driver
    #获取PageXmhtglLogin对象
    def page_get_PageXmglhtLogin(self):
        return PageXmglhtLogin(self.driver)