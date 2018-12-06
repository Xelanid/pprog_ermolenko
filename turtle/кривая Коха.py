import turtle
t = turtle.Turtle()
t.shape("turtle")

t.penup()
t.goto(-200, 0)
t.pendown()


def draw(l, n):
    if n == 0:
        t.forward(l)
        return
    a = l / 3
    draw(a, n - 1)
    t.left(60)
    draw(a, n - 1)
    t.right(120)
    draw(a, n - 1)
    t.left(60)
    draw(a, n-1)


draw(200, 3)
