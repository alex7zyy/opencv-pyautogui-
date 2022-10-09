from time import sleep
import pyautogui
from PIL import ImageGrab, Image
import pyscreeze
import cv2
from os import remove
from tkinter import messagebox


for num in range(1,9):

    sleep(2.3)

    if num == 5:
            pyautogui.click(70,455)
            sleep(2)
            pyautogui.scroll(-1500)
            continue
    elif num == 6:
        sleep(8)
    elif num == 8:
            pyautogui.press('F12')
            sleep(2)

    # 屏幕缩放系数 mac缩放是2 windows一般是1
    screenScale=1

    #事先读取按钮截图
    target= cv2.imread(rf"0{num}.png",cv2.IMREAD_GRAYSCALE)
    # 先截图
    screenshot=pyscreeze.screenshot('my_screenshot.png')
    # 读取图片 灰色会快
    temp = cv2.imread(r'my_screenshot.png',cv2.IMREAD_GRAYSCALE)

    theight, twidth = target.shape[:2]
    tempheight, tempwidth = temp.shape[:2]
    # print("目标图宽高："+str(twidth)+"-"+str(theight))
    # print("模板图宽高："+str(tempwidth)+"-"+str(tempheight))
    # 先缩放屏幕截图 INTER_LINEAR INTER_AREA
    scaleTemp=cv2.resize(temp, (int(tempwidth / screenScale), int(tempheight / screenScale)))
    stempheight, stempwidth = scaleTemp.shape[:2]
    # print("缩放后模板图宽高："+str(stempwidth)+"-"+str(stempheight))
    # 匹配图片
    res = cv2.matchTemplate(scaleTemp, target, cv2.TM_CCOEFF_NORMED)
    mn_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if(max_val>=0.9):
        if num == 8:
            messagebox.showinfo('提示','打卡成功')
            pyautogui.click(1347, 15)
            break
        # 计算出中心点
        top_left = max_loc
        bottom_right = (top_left[0] + twidth, top_left[1] + theight)
        tagHalfW=int(twidth/2)
        tagHalfH=int(theight/2)
        tagCenterX=top_left[0]+tagHalfW
        tagCenterY=top_left[1]+tagHalfH
        #左键点击屏幕上的这个位置
        pyautogui.click(tagCenterX,tagCenterY,button='left')
        remove('my_screenshot.png')
        

        if num == 3:
            pyautogui.typewrite('yqtb.sut.edu.cn/\n')
        elif num == 4:
            sleep(2)
            pyautogui.press('F12')
        elif num == 6:
            sleep(3)
            pyautogui.click(291,594)
        
        
    else:
        if num == 2:
            continue
        
        messagebox.showinfo('打卡提示',f"第{num}步发生错误")
        break

