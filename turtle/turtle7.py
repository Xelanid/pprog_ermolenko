import turtle
t = turtle.Turtle()
t.shape('turtle')
i = 1

for _ in range(200):
    t.forward(i)
    t.left(20)
    i = i + 0.1
