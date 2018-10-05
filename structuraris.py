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
