from tkinter import *
from random import randrange as rnd, choice
import math

root = Tk()
root.geometry('800x600')
width = 600
height = 800

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'gray', 'black']

#cannon - пушка  shell - снаряд target - летающая цель


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = r
        self.color = choice(colors)
        self.dx = dx
        self.dy = dy
        self.points = 0
        self.circle = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)
        self.result = canv.create_text(self.x, self.y, text = self.points)

    def draw(self):
        canv.coords(self.circle, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        #canv.coords(self.result, self.x, self.y)
        #canv.itemconfig(self.result, text = self.points)

    def move(self):
        if (self.x + self.r + self.dx >= width) or (self.x - self.r + self.dx <= 0):
            self.dx = -self.dx
        if (self.y + self.r + self.dy >= height) or (self.y - self.r + self.dy <= 0):
            self.dy = -self.dy

    def collision(self, ball):
        if abs(ball.x - self.x) <= (self.r + ball.r) and abs(ball.y - self.y) <= (self.r + ball.r):
            return True
        else:
            return False
        #a = abs(self.x + self.dx - ball.x)
        #b = abs(self.y + self.dy - ball.y)
        #return (a * a + b * b) ** 0.5 <= self.r + ball.r


class Gun:
    def __init__(self):
        self.power = 10
        self.on = 0
        self.angle = 1
        self.cannon = canv.create_line(20, 450, 50, 420, width=7)

    def begin_shoot(self, event):
        self.on = 1

    def end_shoot(self, event):
        global balls, bullet
        bullet += 1
        new_ball = Ball
        new_ball.r += 3
        self.angle = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.dx = self.power * math.cos(self.angle)
        new_ball.dy = -self.power * math.sin(self.angle)
        balls.append(new_ball)
        self.on = 0
        self.power = 10

    def targetting(self, event=0):
        if event:
            self.angle = math.atan((event.y - 450) / (event.x - 20))
        if self.on:
            canv.itemconfig(self.cannon, fill='orange')
        else:
            canv.itemconfig(self.cannon, fill='black')
        canv.coords(self.cannon, 20, 450, 20 + max(self.power, 20) * math.cos(self.angle),
                    450 + max(self.power, 20) * math.sin(self.angle))

    def power_up(self):
        if self.on:
            if self.power < 100:
                self.power += 1
            canv.itemconfig(self.cannon, fill='orange')
        else:
            canv.itemconfig(self.cannon, fill='black')


mainloop()