import turtle as t

devil = t.Turtle()
devil.shape("turtle")
devil.up()
devil.speed(0)
devil.goto(0,50)

food = t.Turtle()
food.shape("circle")
food.up()
food.goto(0,-100)
food.color("green")

def turnup () :
	t.setheading(90)
	
def turndown () : 
	t.setheading(270)
	
def turnleft () : 
	t.setheading(0)
	
def turnright () : 
	t.setheading(180)

def play() :
	a = devil.towardst(t.pos())
	devil.setheading(a)
	t.fd(6)
	devil.fd(5)
	

t.shape ('turtle')
t.color("white")
t.bgcolor("yellow")
t.speed(0)
t.up()
t.setup(500,500)
t.onkeypress(turnup,'Up')
t.onkeypress(turndown,'Down')
t.onkeypress(turnright,'Right')
t.onkeypress(turnleft,'Left')
t.listen()

t.mainloop()
	
