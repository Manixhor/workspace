def parser(input_line):
	lower_line = input_line.strip().lower()
	
	if lower_line == "true":
		return True, "bool"
	if lower_line == "false":
		return False, "bool"
	
	try:
		if '.' in input_line:
			value = float(input_line)
			return value, "float"
		else:
			value = int(input_line)
			return value, "int"
	except ValueError:
		return input_line, "str"

print(parser("23"))
print(parser("12.3"))
print(parser("True"))
print(parser("false"))
print(parser("My Name"))
		