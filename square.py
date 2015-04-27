global y 

def square(x):
	y = x*x
	print('{0} squared is {1}'.format(x,y))
	return(y)
	
c = square(10)
print(c)

def cube(x):
	y = x*x*x
	print('{0} cubed is {1}'.format(x,y))
	return(y)