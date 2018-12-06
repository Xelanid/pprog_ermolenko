import robot
r = robot.rmap()
r.lm('task4')

while not r.wr():
    r.right()

while not r.wu():
    r.up()

r.left()
r.down()

for _ in range(5):
    for _ in range(2):
        r.pt()
        r.down()
        r.down()
    r.pt()
    r.up(4)
    r.left()
    r.down()
