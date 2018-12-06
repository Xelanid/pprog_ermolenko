import turtle
t = turtle.Turtle()
t.shape('turtle')

Number = 100
Step = 5


def circle(Number, Step):
    for step in range(Number):
        t.forward(Step)
        t.left(360/Number)
    for step in range(Number):
        t.forward(Step)
        t.right(360/Number)
        

for _ in range(3):
    circle(Number, Step)
    t.left(60)
