# Python3
# Code By : القرصان الإلكتروني للتعليم
# My Blog : https://thedigitalagee.blogspot.com
# My Ch Youtube : https://www.youtube.com/krsan4learn

import pyautogui
from time import sleep

msg = input("Enter Your Msg >> :")
num_msg = int(input("Chose Your Numbr of Msg >> :"))
time_msg = float(input("Chose Your Time Of Msg >> :"))

for num in range(num_msg + 1 ):
    pyautogui.typewrite(msg)
    sleep(time_msg)
    pyautogui.press('enter')
    sleep(time_msg)