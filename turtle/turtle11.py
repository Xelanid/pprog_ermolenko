import turtle
t = turtle.Turtle()
t.shape('turtle')
N = 100
L = 5


def circle(N, L):
    for step in range(N):
        t.forward(L)
        t.left(360/N)
    for step in range(N):
        t.forward(L)
        t.right(360/N)


for _ in range(10):
    circle(N, L)
    N = N + 10
