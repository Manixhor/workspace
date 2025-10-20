list = [2,3,1,4,2,1,7]

result = []
for i in list:
	if i not in result:
		result.append(i)
		
print(result)