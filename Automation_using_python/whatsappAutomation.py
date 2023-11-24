import pyautogui
import time
from datetime import datetime
time.sleep(3)
now = datetime.now()
n1 = datetime.now()
count = 1
while((now-n1).seconds<=30):
    now = datetime.now()
    pyautogui.typewrite(str(count)+ ") You ask")
    pyautogui.press("enter")
    count=count+1