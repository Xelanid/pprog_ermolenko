import robot
r = robot.rmap()
r.lm('task1')


def task():
    r.up()
    r.right()
    r.down()
    r.right()
    r.up()
    r.right()
    r.down()


r.start(task)