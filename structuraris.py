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
