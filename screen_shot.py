import time
import pyautogui


def screens_shot():
    time.sleep(5)
    img = pyautogui.screenshot('test.png')
    img.show()


screens_shot()