
word = "fndjnk"

count = {} 

for letter in word:
    if letter in count:
        count[letter] += 1
    else:
        count[letter] = 1

print(count)