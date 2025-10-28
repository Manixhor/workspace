

def wordd():
    word = "mani"
    count = 0
    vowels = "aeiou"
    for letter in word:
        if letter in vowels:
            count += 1
    return(count)
print(wordd())