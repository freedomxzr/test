import os
import sys
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import re
def get_device_name():
    if '\t' in os.popen('adb devices').read() :
        print("已连接")
        a=re.search('\n(.*?)\t',os.popen('adb devices').read())
        #print(a.group())
        device_name=a.group(1)                          #获得device_name
        #device_name=device_name.replace("\n", "")
        #device_name=device_name.replace("\t",'')
        #print(len(device_name))
        print('设备名:',device_name)
        return device_name
    else :
        print("未连接,程序停止")
        os.exit(1)
        return None
get_device_name()