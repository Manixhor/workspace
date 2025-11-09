n = "listen"
n1 = "rammus"

if len(n) != len(n1):
    print("not")

else:
    is_anagram = True
    letters = list(n1)
    for letter in n:
        if letter in letters:
            letters.remove(letter)
        