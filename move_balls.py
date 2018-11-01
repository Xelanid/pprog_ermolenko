from tkinter import *
from random import randrange as rnd, choice
 
root = Tk()
width = 800
height = 600
root.geometry('800x600')
canv = Canvas(bg='white')
canv.pack(fill=BOTH, expand=1)
qty = rnd(3, 10)
balls = []
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'gray', 'black']


for i in range(qty):
    r = rnd(10, 30)
    x = rnd.randint(r, width - r)
    y = rnd.randint(r, height - r)
    dx = rnd.randint(1, 10)
    dy = rnd.randint(1, 10)
    circle = canvas.create_oval(x - r, y - r, x + r, y + r, fill=rnd.choice(colors))
    ball = [x, y, dx, dy, circle]
    balls.append(ball)

 
x0 = rnd(100, 700)
y0 = rnd(100, 500)
 

def balls():
    global x0, y0, circle, speedx, speedy
    x0 += speedx
    y0 += speedy

    if x0 > 750 or x0 < 50: 
        speedx *= -1          
 
    if y0 > 550 or y0 < 50: 
        speedy *= -1
    
    canv.delete(circle)
    circle = canv.create_oval(x0 - r, y0 - r, x0 + r, y0 + r, fill='yellow', width=0)
    root.after(15, balls)


circle = canv.create_oval(-100, 0, 0, 0)
balls()
speedx = 2
speedy = 1
mainloop()