text = "Mmani"
text= text.lower()
freq = {}
for char in text:
	if char in freq:
		freq[char] += 1
	else: 
		freq[char] = 1

print(freq)

from collections import Counter

print(Counter(text))