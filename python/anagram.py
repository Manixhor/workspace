word1 = input()
word2 = input()

if len(word1) != len(word2):
    print("not an anagram")
else:
    #assume as true and take it as list it give every single letter
    
    is_anagram = True
    letters = list(word2)

    for letter in word1:
        if letter in letters:
            letters.remove(letter)
        else:
            is_anagram = False
            break 
    if is_anagram:
        print("yes")
    else:
        print("False")

