#While loop 

i = 1 
while i <= 10:
	i += 1
	print(i)
	
h = 0+1
while h < 6:
	print(f"{h}hello")
	h += 1
	
h = 5 
while h > 0:
	h = h - 1	
	print(h)
while True:
	pass1 = input("enter pass")
	if pass1 == "open123":
		print("Access granted")
		break
	else:
		print("Password is wrong")	
	