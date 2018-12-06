import turtle
t = turtle.Turtle()
t.shape('turtle')
Number = 3
Length = 50
x = 0
y = 0
k = 3

for _ in range(11):
    t.penup()
    t.goto(x, y)
    t.pendown()

    for _ in range(k):
        t.forward(Length)
        t.left(360/Number)

    Number += 1
    Length += 20
    x -= 10
    y -= 7
    k += 1
