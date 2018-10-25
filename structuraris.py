import graphics as gr
import time

window = gr.GraphWin("debri", 700, 700)

trava = gr.Polygon(gr.Point(0, 500), gr.Point(0, 700), gr.Point(700, 700), gr.Point(700, 500))
trava.setFill('green')
trava.draw(window)

sky = gr.Polygon(gr.Point(0, 0), gr.Point(0, 500), gr.Point(700, 500), gr.Point(700, 0))
sky.setFill('blue')
sky.draw(window)

def ball(x, y):
    krug = gr.Circle(gr.Point(x, y), 50)
    krug.setFill('yellow')
    krug.draw(window)

def palka(x, y):
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

def brovi(x, y):
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

cloud1 = gr.Circle(gr.Point(150, 70), 50)
cloud2 = gr.Circle(gr.Point(150 + 30, 70), 50)
cloud3 = gr.Circle(gr.Point(150 - 20, 70 + 20), 50)
cloud4 = gr.Circle(gr.Point(150 + 20, 70 + 20), 50)
cloud5 = gr.Circle(gr.Point(150 + 60, 70 + 20), 50)
cloud1.setFill('gray')
cloud1.draw(window)
cloud2.setFill('gray')
cloud2.draw(window)
cloud3.setFill('gray')
cloud3.draw(window)
cloud4.setFill('gray')
cloud4.draw(window)
cloud5.setFill('gray')
cloud5.draw(window)
    

ball(500, 200)
palka(500, 500)

ball(200, 200)
palka(200, 500)

ball(350, 250)
palka(350, 600)
eyes(350, 250)
brovi(350, 250)
rot(350, 250)



window.getMouse()
while True==True:
    for i in range (100):
        time.sleep(0.01)
        cloud1.move(4,0)
        cloud2.move(4,0)
        cloud3.move(4,0)
        cloud4.move(4,0)
        cloud5.move(4,0)
    for i in range (100):
        time.sleep(0.01)
        cloud1.move(-4,0)
        cloud2.move(-4,0)
        cloud3.move(-4,0)
        cloud4.move(-4,0)
        cloud5.move(-4,0)

window.getMouse()  
window.close()

