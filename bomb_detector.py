import numpy as np
import cv2
import pyautogui as pg
from PIL import Image
from mss.windows import MSS as mss
import time
coords = {'top': 500, 'left': 1119, 'width': 1, 'height': 1}

# def process_screen(screen)

def process_screen(screen):
    processed_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    return processed_screen

def bomb_detector():
    sct = mss()

    while True:
        # time.sleep(5)
        screen = sct.grab(coords)
        screen = np.array(screen)
        screen = process_screen(screen)
        screen = screen[0][0]
        if (screen[0] <= 215 and screen[0] >= 165) and (screen[1] <= 90 and screen[1] >= 10) and (screen[2] <= 90 and screen[2] >= 10):
            print('lol')



# bomb_detector()
