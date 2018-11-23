from tkinter import *
from random import randrange as rnd, choice

root = Tk()
root.geometry('800x600')
width = 600
height = 600
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'gray', 'black']
qty = rnd(7, 15)
balls = []
r = rnd(10, 30)


for j in range(qty):
    x = rnd(r, width - r)
    y = rnd(r, height - r)
    dx = rnd(1, 10)
    dy = rnd(1, 10)
    circle = canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors))
    ball = [x, y, dx, dy, circle]
    balls.append(ball)


def tick_handler():
    global balls
    for i in range(len(balls)):
        x_i, y_i, dx_i, dy_i, circle_i = balls[i]
        x_i += dx_i
        y_i += dy_i
        if x_i < 0:
            dx_i = -dx_i
            x_i = 0
        elif x_i > width - r:
            dx_i = -dx_i
            x_i = width - r
        if y_i < 0:
            dy_i = -dy_i
            y_i = 0
        elif y_i > height - r:
            dy_i = -dy_i
            y_i = height - r
        balls[i] = [x_i, y_i, dx_i, dy_i, circle_i]
        canv.move(circle_i, dx_i, dy_i)


def time_handler():
    global freeze
    speed = speed_scale.get()
    if speed == 0:
        freeze = True
        return
    tick_handler()
    sleep = 1100 - 100 * speed
    root.after(sleep, time_handler)


def unfreezer(event):
    global freeze
    if freeze:
        speed = speed_scale.get()
        if speed != 0:
            freeze = False
            root.after(0, time_handler)


speed_scale = Scale(root, orient=HORIZONTAL, length=300, from_=0, to=10, tickinterval=1, resolution=1)

speed_scale.pack()
speed_scale.set(1)
freeze = False
root.after(10, time_handler)
speed_scale.bind("<Motion>", unfreezer)

root.mainloop()
