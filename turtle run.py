import turtle as t
import random
score = 0
playing = False

devil = t.Turtle()
devil.shape("turtle")
devil.up()
devil.speed(3)
devil.goto(0,-250)
devil.color('orange')

evil = t.Turtle()
evil.shape("turtle")
evil.up()
evil.speed(0)
evil.goto(0,200)
evil.color('purple')

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

def start () :
	global playing
	if playing == False :
		playing = True
		t.clear()
		play()

def play() :
	global score
	global playing
	t.fd(20)
	a = devil.towards(t.pos())
	devil.setheading(a)
	devil.fd(8)
	b = evil.towards(t.pos())
	evil.setheading(b)
	evil.fd(8)
	
	if t.distance(food) < 15 :
		X = random.randint(-250,250)
		Y = random.randint(-250,250)
		food.goto(X,Y)
		score = score +2
		t.write(score)
		
	if score >= 4 :
		devil.fd(10), evil.fd(10)
	elif score >= 8 :
		devil.fd(12), evil.fd(12)
	elif score >= 12 :
		devil.fd(14), evil.fd(14)
	elif score >= 16 :
		devil.fd(16), evil.fd(16)
				
	if t.distance(devil) < 10 or t.distance(evil) < 10 :
		message1("Game Over","Your score is "+str(score))
		playing= False
		score = 0
		food.goto(X,Y)
	
	if playing:
		t.ontimer(play, 100)
		t.up()

def message1(n,m):
	t.up()
	t.color('black')
	t.goto(0,100)
	t.write(n, False, "center", ("",20))
	t.color('black')
	t.goto(0,-100)
	t.write(m, False, "center", ("",10))

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
t.onkeypress(start,'space')
t.listen()
t.title('Turtle Run')

message1 ("WELCOME TURTLE RUN","Tap space to start")
t.mainloop()
	
