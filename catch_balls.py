from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

points = 0
points1 = 0
 
canv = Canvas(root, bg = 'white')
canv.pack(fill = BOTH, expand = 1) 
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'gray', 'black']



def new_ball():
    global x, y, r, circle
    canv.delete(circle)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    
    circle = canv.create_oval(x - r, y - r, x + r, y + r, fill = choice(colors), width = 0)
    root.after(10000, new_ball)

def hit(event):
    global points, result, y, result1, points1
    if (event.y - y)**2 + (event.x - x)**2 <= r**2:
        points += 1
    else:
        points1 += 1 
    y = -1000
    canv.delete(result)
    canv.delete(result1)
    canv.delete(circle)
    result = canv.create_text(180, 20, text = 'Сколько забьет Заболотный: ' + str(points), font = 'Calibri 20')
    result1 = canv.create_text(200, 40, text = 'Сколько пропустит Максименко: ' + str(points1), font = 'Calibri 20')

circle = canv.create_oval(-100,0,0,0)
result = canv.create_text(180, 20, text = 'Сколько забьет Заболотный: ' + str(points), font = 'Calibri 20')
result1 = canv.create_text(200, 40, text = 'Сколько пропустит Максименко: ' + str(points1), font = 'Calibri 20')
points = 0
points1 = 0
canv.bind('<Button-1>', hit)    
new_ball()
mainloop()
