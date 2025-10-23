string = "MANI"

result = ""

for word in string:
	if word not in result:
		result = word + result

print(result)


