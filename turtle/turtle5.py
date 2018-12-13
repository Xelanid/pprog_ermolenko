import turtle

turtle.shape('turtle')
length = 20
for step in range(10):
	for step in range(4):
		turtle.fd(length)
		turtle.rt(90)
	length += 10
	turtle.penup()
	turtle.lt(90)
	turtle.fd(5)
	turtle.rt(90)
	turtle.backward(5)
	turtle.pendown()
	
