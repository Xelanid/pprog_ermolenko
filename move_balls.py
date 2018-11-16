from tkinter import *
from random import randrange as rnd, choice

root = Tk()
root.geometry('800x600')
width = 600
height = 800

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'gray', 'black']
qty = rnd(3, 10)
balls = []
r = rnd(10, 30)


for i in range(qty):
    x = rnd(r, width - r)
    y = rnd(r, height - r)
    dx = rnd(1, 10)
    dy = rnd(1, 10)
    circle = canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors))
    ball = [x, y, dx, dy, r, circle]
    balls.append(ball)


x0 = rnd(100, 700)
y0 = rnd(100, 500)


def balls():
    global x0, y0, circle, x, y
    x0 += x
    y0 += y
    if x0 > 750 or x0 < 50:
        x *= -1
    if y0 > 550 or y0 < 50:
        y *= -1


canv.delete(circle)
circle = canv.create_oval(x0 - r, y0 - r, x0 + r, y0 + r, fill='yellow', width=0)
root.after(15, balls)
circle = canv.create_oval(-100, 0, 0, 0)
balls()
x = 2
y = 1
mainloop()