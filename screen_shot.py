import time
import pyautogui


def screens_shot():
    name = int(round(time.time()*1000))
    name = '{}.png'.format(name)
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()


screens_shot()