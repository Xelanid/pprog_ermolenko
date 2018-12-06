import turtle
t = turtle.Turtle()
t.shape('turtle')


def circle(x, y):
        for _ in range(180):
                t.forward(x)
                t.right(1)
        for _ in range(180):
                t.forward(y)
                t.right(1)
        

turtle.left(90)

for _ in range(3):
        circle(0.5, 0.1)
