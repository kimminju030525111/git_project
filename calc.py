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
	return(A)
print(calc())
