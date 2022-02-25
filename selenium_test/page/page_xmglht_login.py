from time import sleep

from base.base import Base, log
import page

class PageXmglhtLogin(Base):
    '''
    1.
    '''
    def page_input_username(self,username):#输入用户名
        self.base_input(page.xmglht_username,username)#调用父类中的输入方法
    def page_input_password(self,password):#输入密码
        self.base_input(page.xmglht_password,password)#调用父类中的输入方法
    def page_click_login_btn(self):
        self.base_chilk(page.xmglht_login_btn)#调用父类的点击方法
    def page_get_nickname(self):
        '''用于脚本断言层服务'''
        return self.base_get_text(page.xmglht_nickname)#获取父类获取text方法,并返回
    def page_xmhtgl_login(self,username,password):
        '''
        提示调用相同页面操作步骤,跨页面暂时不考虑
        组合成一个方法,用于测试脚本层调用
        :return:
        '''
        log.info("正在调用项目管理后台的登录方法，用户名:{}\t密码:{}".format(username,password))
        sleep(1)
        self.page_input_username(username)
        self.page_input_password(password)
        sleep(1)
        self.page_click_login_btn()

