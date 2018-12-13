import turtle
t = turtle.Turtle()
t.shape('turtle')
step = 1

for j in range(200):
    t.forward(step)
    t.left(20)
    step += 0.1
