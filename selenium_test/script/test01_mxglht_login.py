import pytest

from base.base import log
from page.page_in import PageIn
from tools.read_yaml import read_yaml

from tools.get_driver import GetDriver
import page
class TestXmglhtLogin:
    def setup_class(self):#初始化
        '''1.获取driver(统一入口类需要先获取driver)2.通过统一入口类获取对象'''
        driver=GetDriver.get_web_driver(page.url_xmglht)
        self.xmhtgl=PageIn(driver).page_get_PageXmglhtLogin()
    def teardown_class(self):#结束,关闭driver
        GetDriver.quit_web_driver()
    @pytest.mark.parametrize("username,password,expect",read_yaml("xmglht_login.yaml"))
    def test_xmglht_login(self,username,password,expect): #业务方法
        '''
        1.调用登录业务方法
        2.断言
        :return:
        '''
        self.xmhtgl.page_xmhtgl_login(username,password)
        try:
            assert self.xmhtgl.page_get_nickname()==expect
        except AssertionError as e:
            log.error("断言失败,错误信息:{},正在截图错误页面".format(e))
            self.xmhtgl.base_get_img()
            raise


