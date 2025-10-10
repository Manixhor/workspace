def my_max(num):
	biggest = num[0]
	for number in num:
		if number > biggest:
			biggest = number
	return biggest
	
def my_min(num):
	smallest = num[0]
	for number in num:
		if number < smallest:
			smallest = number
	return smallest 
def my_sum(num):
	total = 0 
	for num in num:
		total = total + num
	return total
num = [1,2,3,4,5,6]
print(my_max(num))
print(my_min(num))
print(my_sum(num))