import robot
r = robot.rmap()
r.lm('task5')

for _ in range(3):
    for _ in range(8):
        r.pt()
        r.right(2)

    r.down()

    for _ in range(3):
        r.left()
        r.pt()
        r.left(3)

    r.left()
    r.pt()
    r.left()
    r.down(2)