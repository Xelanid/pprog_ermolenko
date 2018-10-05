import graphics as gr

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

def glaza(x, y):
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
    mouth.draw(window)

def oblaka(x, y, r):
    oblako = gr.Circle(gr.Point(x, y), r)
    oblako.setFill('gray')
    oblako.draw(window)
    

ball(500, 200)
palka(500, 500)

ball(200, 200)
palka(200, 500)

ball(350, 250)
palka(350, 600)
glaza(350, 250)
brovi(350, 250)
rot(350, 250)

oblaka(150, 70, 50)
oblaka(180, 70, 50)
oblaka(130, 90, 50)
oblaka(170, 90, 50)
oblaka(210, 90, 50)



    
