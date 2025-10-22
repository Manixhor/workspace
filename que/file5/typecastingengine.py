def adding_intoabox(values,t_type):
	result = []
	for value in values:
		try:
			result.append(t_type(value))
		except:
			result.append(value)
	xreturn result
			
values = ["1","46","Mani","23.4"]
print(adding_intoabox(values, int))