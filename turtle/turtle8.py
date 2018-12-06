import turtle
t = turtle.Turtle()
t.shape('turtle')
i = 20

for _ in range(50):
    t.forward(i)
    t.left(90)
    i = i + 10
