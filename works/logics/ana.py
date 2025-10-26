word1 = "lis"
word2 = "sil"
if len(word1) != len(word2):
	print("not")
else:
	is_anagram = True 
	letters = list(word2)
	
	for letter in word1:
		if letter in letters:
			letters.remove(letter)
		else:
			is_anagram = False
			break
	if is_anagram:
		print("true")