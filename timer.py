import time
from tkinter import *
class Timer:
    def __init__(self, secs):
        self.secs = secs
        self.window = Tk()
        self.lbl = Label(self.window, text = 'lol')
        self.lbl.grid(column = 0, row = 0)

    def start(self):
        copy = self.secs
        while copy != 0:
            self.window.mainloop()
            print(copy)
            copy -= 1
            time.sleep(1)



timer = Timer(10)
timer.start()


