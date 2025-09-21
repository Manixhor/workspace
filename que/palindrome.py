word = input()

word = word.lower()

reversed_word = ""
for letter in word:
    reversed_word = letter + reversed_word

if word == reversed_word:
    print("yes")

else:
    print("Nope")
    