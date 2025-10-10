def datatype(sortingmachine):
	result = {
		'int' :0,'float': 0,'str': 0,'bool': 0
	}
	for item in sortingmachine:
		if type(item) == int:
			result['int'] += 1
		elif type(item) == float:
			result['float'] += 1
		elif type(item) == str:
			result['str'] += 1
		elif type(item) == bool:
			result['bool'] += 1
	return result 
	
sortingmachine = [10,"helloworld","whatthe",3.14,True,42,False,"dvbfejkf2"]
print(datatype(sortingmachine))