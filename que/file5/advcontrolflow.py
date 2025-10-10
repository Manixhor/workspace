def filter(numbers):
	result = []
	for num in numbers:
		if num < 0:
			break
		elif num % 3 == 0:
			continue
		result.append(num)
	return result 

print(filter([1,2,3,4,5,6,-0,1]))