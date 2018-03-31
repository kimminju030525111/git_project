import turtle as t
import random
devil = t.Turtle()
devil.shape("turtle")
devil.up()
devil.speed(3)
devil.goto(0,-250)
devil.color('red')

evil = t.Turtle()
evil.shape("turtle")
evil.up()
evil.speed(0)
evil.goto(0,200)

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
	t.setheading(180)
	
def turnright () : 
	t.setheading(0)

def play() :
	t.fd(6)
	a = devil.towards(t.pos())
	devil.setheading(a)
	devil.fd(5)
	b = evil.towards(t.pos())
	evil.setheading(b)
	evil.fd(5)
	
	if t.distance(food) < 10 :
		X = random.randint(-250,250)
		Y = random.randint(-250,250)
		food.goto(X,Y)
	
	if t.distance(devil) and t.distance(evil) > 10 :
		t.ontimer(play, 100)	
		
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
t.onkeypress(play,'space')
t.listen()
play()

t.mainloop()
	
