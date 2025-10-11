text = "qwertyuioplkjhgfdsazxcvbnm"

def remove_vow(s):
	vowels = "aeiousAEIOU"
	result = ""
	for letter in s:
		if letter not in vowels:
			result += letter
	return result
print("removed the vowels:",remove_vow(text))

def count1(s):
	freq = {}
	for letter in s:
		if letter in freq:
			freq[letter] += 1
		else:
			freq[letter] = 1
	return freq 
print("counting the text:",count1(text))

def substrings(s,k):
	result = []
	for i in range(len(s) - k + 1):
		result.append(s[i:i+k])
	return result 
print("substring:",substrings(text, 3))
