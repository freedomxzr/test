import os
from appium import webdriver
import re
from time import sleep
import sys
def arg_erro():
    try:
        if eval(sys.argv[1]) not in [0,1]:
            print(sys.argv[1],type(sys.argv[1]))
            ex=Exception("输入信息有误,0:表示上班打卡,1:表示下班打卡")
            raise ex
        elif eval(sys.argv[1])==1:
            print ('正在进行',sys.argv[1],'下班!')
        else:
            print ('正在进行',sys.argv[0],"上班!")
    except :
        print("输入参数错误退出程序!")     
        sys.exit(0)
        
def get_platformVersion():
    platfromVersion=os.popen('adb shell getprop ro.build.version.release').read().replace("\n","")
    print("安卓版本为:",platfromVersion)
    return platfromVersion 
    
def set_up():
    print ("0:上班打卡,1:下班打卡")
    arg_erro()

def get_am_time():
    a=driver.find_element_by_android_uiautomator('new UiSelector().resourceId("btnyqd")')
    b=a.find_element_by_xpath('//android.view.View[2]')
    print (b.get_attribute("resource-id"),":(上班打卡时间)",b.get_attribute('text'))

def get_pm_time():   #必须保证已打卡状态,否者b元素不存在!
    a=driver.find_element_by_android_uiautomator('new UiSelector().resourceId("btnyqt")')
    b=a.find_element_by_xpath('//android.view.View[2]')
    print (b.get_attribute("resource-id"),":(下班打卡时间)",b.get_attribute('text'))


def log_in():
    try:
        driver.find_element_by_id('com.alibaba.android.rimet:id/et_phone_input').clear()
        driver.find_element_by_id('com.alibaba.android.rimet:id/et_phone_input').send_keys("19906876087")
        driver.find_element_by_id('com.alibaba.android.rimet:id/et_pwd_login').clear()
        driver.find_element_by_id('com.alibaba.android.rimet:id/et_pwd_login').send_keys("xuezhenrui123")
        driver.find_element_by_id('com.alibaba.android.rimet:id/cb_privacy').click()
        driver.find_element_by_id('com.alibaba.android.rimet:id/tv').click()
    except:
        print("已经登录")
def open_appium():
    pass 
       
def unlock_screen():
    #os.popen('adb shell input keyevent 26')
    #sleep(1)
    msg=os.popen('adb shell dumpsys power | find "Display Power: state="').read()
    if msg=='Display Power: state=ON\n':
        sleep(1)
        print('从亮屏状态启动,锁屏操作执行')
        os.popen('adb shell input keyevent 26')        
    else:
        print("从息屏状态启动")       
    dic1 = {       #用来解锁的webdriver参数,暂时只能通过调用webdriver对象解锁
        "platformVersion": platform_version,
        "platformName": "Android",
        "deviceName": device_name,
    }
    try:
        os.popen('adb shell input keyevent 26')
        driver1 = webdriver.Remote("http://127.0.0.1:4723/wd/hub", dic1)
        driver1.implicitly_wait(3)
        os.popen('adb shell input swipe 500 1800 500 100 100')
        sleep(1)
        driver1.find_element_by_accessibility_id("1").click()
        driver1.find_element_by_accessibility_id("2").click()
        driver1.find_element_by_accessibility_id("3").click()
        driver1.find_element_by_accessibility_id("4").click()
        driver1.find_element_by_accessibility_id("5").click()
        driver1.find_element_by_accessibility_id("6").click()
        driver1.quit()
    except Exception as err_msg:
        print(err_msg)
        print("创建webdriver出错,")
        #open_appium()
def err_screencap(msg):
    print(msg)
    os.popen('adb shell screencap -p /sdcard/错误异常.png')
    sleep(1)
    os.popen('adb pull /sdcard/错误异常.png E:错误异常.png')
    os.popen('adb pull /sdcard/错误异常.png E:result.png')
    print("程序遇到未处理的异常,提早结束运行!")
    sleep(1)
def check_update():
    el_update=driver.find_element_by_class_name("android.support.v7.widget.LinearLayoutCompat")
    print("存在更新框,选择取消")
    driver.find_element_by_class_name('android.widget.Button')[1].click()  


#校验是否锁定屏幕,true表示锁屏,false表示解锁状态
def screen_is_lock():
    msg=re.search('mInputRestricted=true',os.popen('adb shell dumpsys window policy |find "mInputRestricted"').read())
    if msg !=None:
        print('锁定状态:',msg.group(),'ture表示锁住了')
        return True
    else:
        print('解锁状态,后续先执行锁屏在执行解锁流程')
        return False

#driver_name
def get_device_name():
    if '\t' in os.popen('adb devices').read() :
        print("已连接")
        a=re.search('\n.*\t',os.popen('adb devices').read())
        #print(a.group())
        device_name=a.group()                          #获得device_name
        device_name=device_name.replace("\n", "")
        device_name=device_name.replace("\t",'')
        #print(len(device_name))
        print('设备名:',device_name)
        return device_name
    else :
        print("未连接,程序停止")
        os.exit(0)
        return None

def punch_card():
    el1 = driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("com.alibaba.android.rimet:id/home_bottom_tab_icon_group")')
    el1[2].click()
    sleep(3)
    el2 = driver.find_element_by_android_uiautomator('new UiSelector().text("去打卡")') 
    el2.click()
    

#开始执行!
set_up()
device_name=get_device_name()
platform_version=get_platformVersion()
try:
    if screen_is_lock() :
        unlock_screen()
    else:
        os.popen('adb shell input keyevent 26')
        sleep(1)
        unlock_screen()
except Exception as screen_ex:
    err_screencap(screen_ex)
    ex=Exception("为了重构而创建的异常")
    raise ex


#初始化钉钉参数
dic = {
"platformVersion": "10",
"platformName": "Android",
"deviceName": device_name,
"appPackage": "com.alibaba.android.rimet",
"appActivity": "com.alibaba.android.rimet.biz.LaunchHomeActivity",
"noReset": True,
"unicodeKeyboard": True,
"resetKeyboard": True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", dic)
driver.implicitly_wait(5)
try :
    log_in()
except Exception as err_log_in:
    err_screencap(err_log_in)
    ex=Exception("为了重构而创建的异常")
    raise ex
    
try:
    check_update()
except :
    print("不需要更新!")
try :
    punch_card()
except Exception as err_punch_card:
    err_screencap(err_punch_card)
    ex=Exception("为了重构而创建的异常")
    raise ex

    
    
try:
    x=driver.get_window_size()['width']
    y=driver.get_window_size()['height']
    print("x:%d,y:%d" % (x,y))
    sleep(3)
    if eval(sys.argv[1])==0:
        print('准备上班')
        #driver.tap([(0.8231*x,0.8658*y)])#签到
        try:
            elsb=driver.find_element_by_android_uiautomator('new UiSelector().resourceId("btnqd")')
            if elsb.get_attribute("text") == "签到":
                elsb.click()
        except:
            elsb=driver.find_element_by_android_uiautomator('new UiSelector().resourceId("btnyqd")')
            get_am_time()
        print("上班打卡成功!")
        sleep(1)
    else:
        print('准备下班!')
        #driver.tap([(0.8231*x,0.9453*y)])#签退
        try:
            elgx=driver.find_element_by_android_uiautomator('new UiSelector().text("更新签退")')
            #get_pm_time()
            print("更新打卡时间")
            elgx.click()
            #driver.find_element_by_android_uiautomator('new UiSelector().resourceId("android:id/button1")').click()    #弹窗确定元素
        except:
            print("首次打卡!")
            elxb=driver.find_element_by_android_uiautomator('new UiSelector().resourceId("btnqt")')
            elxb.click()
            sleep(3)
        print("下班打卡成功!")
        sleep(1)
except Exception as excp_main:
    print('打卡失败,出现错误')
    print(excp_main)
    print("异常出现的位置",excp_main.__traceback__.tb_lineno)
    os.popen('adb shell screencap -p /sdcard/打卡页面异常.png')
    sleep(1) 
    os.popen('adb pull /sdcard/打卡页面异常.png E:打卡页面异常.png')
    os.popen('adb pull /sdcard/打卡页面异常.png E:result.png')


# # 897 1855   签到
# # 889 2022  qiantui
# #  x:1080,y:2139

os.popen('adb shell screencap -p /sdcard/success.png')
sleep(1)
os.popen('adb pull /sdcard/success.png E:success.png')
os.popen('adb pull /sdcard/success.png E:result.png')
sleep(5)
driver.quit()
os.popen('adb shell input keyevent 26')   