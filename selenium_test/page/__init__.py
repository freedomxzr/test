'''以下数据为项目管理后台模块配置数据以及后台管理url
能用css选择器的尽量不使用xpath
无需加@
'''

from selenium.webdriver.common.by import By
#项目管理后台元素
xmglht_username=(By.CSS_SELECTOR,'[placeholder="账号"]')#用户名
xmglht_password=(By.CSS_SELECTOR,'[placeholder="密码"]')#密码
#验证码
xmglht_login_btn=(By.CSS_SELECTOR,'[class="el-button el-button--primary"]')#登录按钮
xmglht_nickname=(By.CSS_SELECTOR,'.el-dropdown-link')#昵称

url_xmglht ="https://greenshop-uat.gtdreamlife.com/operation#/index/login"