def unique(s):
	chars = set(s)
	vowels = set("aeiouAEIOUS")
	return chars - vowels
print(unique("applemac1"))