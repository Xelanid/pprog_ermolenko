import turtle
t = turtle.Turtle()
t.shape('turtle')
length = 20

for i in range(50):
    t.forward(length)
    t.left(90)
    length += 10
