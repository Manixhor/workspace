def prime_num(n):
	for num in range(2, n + 1):
		for i in range(2,num):
			if num % i == 0:
				break
		else:
			yield num
	
for p in prime_num(10):
	print(p)