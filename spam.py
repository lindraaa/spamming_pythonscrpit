import pyautogui
import time

message = "pake ko sayo"
n = 10

time.sleep(2)

for i in range(n):
    pyautogui.typewrite(message+" ")
