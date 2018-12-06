import turtle
t = turtle.Turtle()
t.shape('turtle')
i = 20

for _ in range(10):
    for _ in range(4):
        turtle.forward(i)
        turtle.left(90)

    i = i + 10
    t.penup()
    t.right(90)
    t.forward(5)
    t.right(90)
    t.forward(5)
    t.right(180)
    t.pendown()
