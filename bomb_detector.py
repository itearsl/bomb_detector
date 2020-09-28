import numpy as np
import cv2
import pyautogui as pg
from PIL import Image
from mss.windows import MSS as mss
import time
from tkinter import *
coords = {'top': 7, 'left': 675, 'width': 1, 'height': 1}

sct = mss()
t_start = 40
after_id_tick = ''
after_id_det = ''

def start_handler():
    btn_start.grid_forget()
    main.wm_attributes("-disabled", True)
    main.wm_attributes("-transparentcolor", "green")
    main.attributes("-topmost", True)
    main.overrideredirect(True)
    main.lift()
    timer_label.configure(bg = "green")
    bomb_detector()

def tick():
    global t_time, after_id_tick, t_start
    after_id_tick = main.after(1000, tick)
    if t_start == -1:
        t_start = 40
        timer_label.configure(text=str(t_start))
        main.after_cancel(after_id_tick)
        bomb_detector()
        return
    timer_label.configure(text = str(t_start))
    t_start -= 1




def process_screen(screen):
    processed_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    return processed_screen



def bomb_detector():
    global  after_id_det
    after_id_det = main.after(0, bomb_detector)
    screen = sct.grab(coords)
    screen = np.array(screen)
    screen = process_screen(screen)
    screen = screen[0][0]
    if (screen[0] <= 215 and screen[0] >= 165) and (screen[1] <= 90 and screen[1] >= 10) and (screen[2] <= 90 and screen[2] >= 10):
        main.after_cancel(after_id_det)
        tick()


main = Tk()
main.title("lol")
main.geometry('-50+0')

timer_label = Label(main, width = 5, font=["Comic Sans MS", 15], text = '40', fg = '#32CD32')
timer_label.grid(row =0, columnspan = 2)
btn_start = Button(font=["Comic Sans MS", 5], text = 'start', command = start_handler)
btn_start.grid(row =1, columnspan = 2, sticky = "ew")


main.mainloop()
