# 계산기 프로그램
import random as r

def calc():
	first = r.randint(0,100)
	middle = r.randint(1,3)
	last = r.randint(0,100)

	if middle == 1 :
		k = '+'
	elif middle == 2 :
		k = '-'
	elif middle == 3 :
		k = '*' 
	
	A = str(first) + k + str(last)
	return A

while  True : 
	B = calc()
	num = input(B+ '=')
	if int(num) != eval(B) :
		print('틀렸습니다.')
	else :
		print('정답입니다.')
		
	C = input('계속 진행하시겠습니까? Y/N')
	if C == 'Y' :
		continue
	else :
		print('감사합니다.')
		break




