import robot
r = robot.rmap()
r.lm('task2')

r.up()
i = 0
for i in range(5):
    r.pt()
    r.right()
    r.up()
    r.pt()
    r.down(2)
    r.pt()
    r.up()
    r.right()
    r.pt()
    r.right()
