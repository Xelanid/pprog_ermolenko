import graphics as gr
import time

window = gr.GraphWin("forest", 700, 700)

field = gr.Polygon(gr.Point(0, 500), gr.Point(0, 700), gr.Point(700, 700), gr.Point(700, 500))
field.setFill('green')
field.draw(window)

sky = gr.Polygon(gr.Point(0, 0), gr.Point(0, 500), gr.Point(700, 500), gr.Point(700, 0))
sky.setFill('blue')
sky.draw(window)


def ball(x, y):
    circle = gr.Circle(gr.Point(x, y), 50)
    circle.setFill('yellow')
    circle.draw(window)


def sticks(x, y):
    stick = gr.Polygon(gr.Point(x - 3, y / 2), gr.Point(x - 3, y), gr.Point(x + 3, y), gr.Point(x + 3, y / 2))
    stick.setFill('black')
    stick.draw(window)


def eyes(x, y):
    eye1 = gr.Circle(gr.Point(x - 25, y - 15), 10)
    eye2 = gr.Circle(gr.Point(x + 22, y - 19), 15)
    eye1_center = gr.Circle(gr.Point(x - 25, y - 15), 5)
    eye2_center = gr.Circle(gr.Point(x + 22, y - 19), 7)
    eye1.setFill('red')
    eye2.setFill('red')
    eye1_center.setFill('black')
    eye2_center.setFill('black')
    eye1.draw(window)
    eye2.draw(window)
    eye1_center.draw(window)
    eye2_center.draw(window)


def brow(x, y):
    eyebrow1 = gr.Line(gr.Point(x - 15, y - 30), gr.Point(x - 40, y - 37))
    eyebrow2 = gr.Line(gr.Point(x + 10, y - 40), gr.Point(x + 40, y - 50))
    eyebrow1.setWidth(10)
    eyebrow2.setWidth(10)
    eyebrow1.setOutline('black')
    eyebrow2.setOutline('black')
    eyebrow1.draw(window)
    eyebrow2.draw(window)


def rot(x, y):
    mouth = gr.Line(gr.Point(x - 20, y + 30), gr.Point(x + 20, y + 30))
    mouth.setWidth(10)
    mouth.setOutline('black')


def clouds(x, y, r):
    cloud1 = gr.Circle(gr.Point(150, 70), 50)
    cloud2 = gr.Circle(gr.Point(150 + 30, 70), 50)
    cloud3 = gr.Circle(gr.Point(150 - 20, 70 + 20), 50)
    cloud4 = gr.Circle(gr.Point(150 + 20, 70 + 20), 50)
    cloud5 = gr.Circle(gr.Point(150 + 60, 70 + 20), 50)
    cloud = [cloud1, cloud2, cloud3, cloud4, cloud5]
    i = 1
    for i in range(5):
        cloud[i].setFill('gray')
        cloud[i].draw(window)


ball(500, 200)
sticks(500, 500)

ball(200, 200)
sticks(200, 500)

ball(350, 250)
sticks(350, 600)
eyes(350, 250)
brow(350, 250)
rot(350, 250)

clouds(150, 70, 50)

window.getMouse()  
window.close()

