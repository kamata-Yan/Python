from math import sqrt

def fun(x):
	return x*x

x = int(input())

for i in range(20):
	e = 0
	if(i%2==0 and x<0):
		e = i/2*sqrt(abs(fun(x)))
	elif(i%2!=0 and x>0):
		e = i*sqrt(fun(x))
	else:
		e = sqrt(abs(i*fun(x)))
	print("значение ", e)