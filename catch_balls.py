from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')
 
canv = Canvas(root, bg = 'white')
canv.pack(fill = BOTH, expand = 1)
 
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'gray', 'black']

def left_click(event):
    print('left click')
    x = event.x
    y = event.y
    r = rnd(30,50)
    canv.create_oval(x - r, y - r, x + r, y + r, fill = choice(colors), width = 0)
    

def right_click(event):
    print('right click')
    canv.delete(ALL)

canv.bind('<Button-1>', left_click)
canv.bind('<Button-3>', right_click)

mainloop()
