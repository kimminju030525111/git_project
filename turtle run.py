import turtle as t

devil = t.turtle()
devil.shape("turtle")
devil.up()
devil.speed(0)
devil.goto(0,50)

food = t.turtle()
food.shape("circle")
food.up()
food.goto(0,-100)

def turnup () :
	t.setheading(90)
	
def turndown () : 
	t.setheading(270)
	
def turnleft () : 
	t.setheading(0)
	
def turnright () : 
	t.setheading(180)

t.shape ('turtle')
t.color("white")
t.bgcolor("yellow")
t.speed(0)
t.up()
t.setup(500,500)
t.onkeypress(up,'up')
t.onkeypress(down,'down')
t.onkeypress(right,'right')
t.onkeypress(left,'left')
t.listen()
t.goto()

	
