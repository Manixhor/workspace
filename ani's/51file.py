def table(num):
	for i in range(1,11):
		result = num * i 
		print(f"{num} * {i} = {result}")

n = int(input(	))	
table(n)


#odd or even 

def find(n):
	if n % 2 == 0:
		print("it's even")
	else:
		print("odd")

find(n)