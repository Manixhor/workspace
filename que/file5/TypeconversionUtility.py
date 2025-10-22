def convert_types(data):
	new_data = {}
	for key, value in data.items():
		if value.isdigit():
			new_data[key] = int(value)
		elif value.replace('.',' ',1).isdigit() and value.count('.') < 2:
			new_data[key] = float(value)
		elif value == "True":
			new_data[key] = True
		elif value == "False":
			new_data[key] = False
		else:
			new_data[key] = value
	return new_data
	
info = {
	"age": "10",
	"height":"5.5",
	"is_tall": "True",
	"Name": "Alex",
	"is_weight": "False"
}

print(convert_types(info))