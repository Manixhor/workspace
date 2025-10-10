def remove(s):
	vowels = "aeiouAEIOU"
	result = ""
	for char in s:
		if char not in vowels:
			result += char 
	return result 
		
s = "Mani"
print(remove(s))