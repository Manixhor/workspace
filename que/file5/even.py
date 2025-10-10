#finding even  numbers 
list1 = [11,2,3,4,5,6,7,8,9,]

for i in list1:
	if  i%2 == 0:
		print(i)
print("------End of even numbers-------")
#to square all odd numbers 
 
for i in list1:
	if i%2 != 0:
		print(i*i)