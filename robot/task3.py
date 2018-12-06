import robot

r = robot.rmap()
r.lm('task3')


def task():
    for i in range(3):
        r.right(2)
        r.dn()
        r.up()

    r.rt(2)


r.start(task)
