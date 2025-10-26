sent = "I love mymackiii"
words = sent.split()

longest = ""
for word in words:
	if len(word) > len(longest):
		longest = word

print(longest)