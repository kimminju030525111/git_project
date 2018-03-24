import turtle as t 
import random 

def up () :
	t.left (2)
	
def down () : 
	t.right (2)

def shot () : 
	# 거북이 포물선으로 발사 후 땅에 닿을 때까지 반복
	ang= t.heading()
	while t.ycor()> 0 :
		t.fd (15)
		t.right (5)
		
	# 타겟과 거북이 거리 차이 확인 후 문구 띄우기	
	d = t.distance(target,0)
	t.sety(random.randint(10,100))
	if d <= 25 :
		t.color('blue')
		t.write("Great",False,"center",("",15))
		
	else :
		t.color('red')
		t.write("Bad",False,"center",("",15))
		
	# 거북이 다시 돌아가기
	t.goto(-200,10)
	t.setheading(ang)
	t.color('black')

# 기본 바탕 설정 및 랜덤 생성	
t. bgcolor('yellow')
t. goto(-300,0)
t. down()
t. goto(300,0)
t. up()
t. color('orange')
t. pensize (20)
t. pencolor('green')
target = random.randint(50,150)
a = target +25
b = target -25
t.goto (a,0)
t.down()
t.goto (b,0)
t.up()
t.color('black')
t.goto(-200,10)
t.onkeypress(up,'Up')
t.onkeypress(down,'Down')
t.onkeypress(shot,'space')
t.listen()
t.mainloop()
