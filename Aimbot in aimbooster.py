from pyautogui import *
import pyautogui
import time
import random
import keyboard
import win32api, win32con

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(375,250,603,421))
    width, height = pic.size
    for x in range(0,603,5):
        for y in range(0,421,5):
            r,g,b = pic.getpixel((x,y))
            if (r,g,b) == (255, 219, 195):
                click(x+375,y+250)
                time.sleep(0.02)
                break
