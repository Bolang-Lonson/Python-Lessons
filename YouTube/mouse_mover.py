import pyautogui as pag
import random
import time

for a in range(0,400,10):
    x=random.randint(600,700)
    y=random.randint(200,600)
    pag.moveTo(x,y,a)
    time.sleep(1)
