import turtle
t = turtle.Turtle()
t.shape('turtle')

for _ in range(12):
    t.forward(100)
    t.stamp()
    t.backward(100)
    t.right(360/12)
