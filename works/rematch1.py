import re		
match = "abscdkcdabc"

pattern = re.compile(r'abc')

matches = pattern.finditer(match)

for match in matches:
	print(match)v