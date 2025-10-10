#Implement a function to check if two strings are anagrams.


word1 = input()
word2 = input()

words = list(word2)
if len(word1) != len(word2):
    print("it's not an anagram")


else:
    is_anagram = True
    for letter in word1:
        if letter in words:
            words.remove(letter)
        else:
            is_anagram = False
            break

if is_anagram:
    print("yes")
else:
    print("No")