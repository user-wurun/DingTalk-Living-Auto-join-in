import os
import time
from ctypes import *
from ctypes import windll

import win32api
import win32con

print('欢迎使用钉钉智能')
print('本软件支持市面上主流的16:9显示器，如果你的长宽比较为特殊，可能该软件并不适合你。')

x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)   #获得屏幕分辨率X轴
y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)   #获得屏幕分辨率Y轴
print("你的分辨率为：",x,"×",y)
sssssss = input('分辨率是否正确？填yes或no')
if sssssss == "no":
    x = int(input('请输入长：'))
    y = int(input('请输入宽：'))
ty = y*10
dy = ty//108
tx = x*100
dx = tx//192

wwwy = y*23
qpy = wwwy//108
wwwx = x*130
qpx = wwwx//192

ass = input('是否开启自动签到是输入y，否输入n：')

if ass == 'y':
    x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)   #获得屏幕分辨率X轴
    y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)   #获得屏幕分辨率Y轴

    ny = y*90
    p = int(ny//108)
    nx = x*140
    o = int(nx//192)
#死循环
while True:
    #取直播颜色
    def get_color(dx, dy):
        gdi32 = windll.gdi32
        user32 = windll.user32
        # 获取颜色值
        hdc = user32.GetDC(None)
        # 提取RGB值
        pixel = gdi32.GetPixel(hdc,dx,dy)  
        r = pixel & 0x0000ff
        g = (pixel & 0x00ff00) >> 8
        b = pixel >> 16
        return [r, g, b]
    #转储RGB值
    m = get_color(dx, dy)
    #RGB值判断
    if m == [224, 237, 254]:
        print('已上课')
        time.sleep(1)
        #移到鼠标
        windll.user32.SetCursorPos(dx,dy)
        time.sleep(1)
        #按下鼠标
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, dx,dy)
        time.sleep(0.05) 
        #抬起鼠标   
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, dx, dy)
        time.sleep(25)
        #全屏
        windll.user32.SetCursorPos(qpx,qpy)
        for i in range(2):
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, qpx,qpy)
            time.sleep(0.05) 
            #抬起鼠标
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, qpx, qpy)
            time.sleep(0.05)
        
    else:
        print('未上课或已进入直播间')
        time.sleep(5)
    #签到确认
    if ass == 'y':
        def get_color(o, p):
                gdi32 = windll.gdi32
                user32 = windll.user32
                # 获取颜色值
                hdc = user32.GetDC(None)
                # 提取RGB值
                pixel = gdi32.GetPixel(hdc, o, p)  
                r = pixel & 0x0000ff
                g = (pixel & 0x00ff00) >> 8
                b = pixel >> 16
                return [r, g, b]
        #转储
        s = get_color(o,p)
        #提值
        e= s[0]
        emm = s[2]
        #颜色取样识别
        #print(s)
        #列表取值
        #print(e)

        if e > 220 and e < 256:
            if emm < 255:
                print('有签到')
                time.sleep(1)
                #移到
                windll.user32.SetCursorPos(o,p)
                #按下
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, o, p)
                time.sleep(0.05)
                #抬起    
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, o, p)
                print('已签到')
            else:
                print('无签到')
                time.sleep(5)
        else:
            print('无签到')
            time.sleep(5)
