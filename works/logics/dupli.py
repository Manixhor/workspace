li = [1,1,2,3,4,2,11,13]

result = []

for i in li:
	if i not in result:
		result.append(i)
		
print(result)