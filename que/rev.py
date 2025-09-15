#reverse a string 

# word = input("enter your word to reverse \n")
# reverse = ""
# for letter in word:
#     reverse = letter + reverse
# print(reverse)


# #find the largest number in a list 

# num = input("number")

# nlist = num.split()
# nlist = [int(num) for num in nlist]
# biggest = nlist[0]

# for num in nlist:
#     if num > biggest:
#         biggest = num 
# print(biggest)

#now no input

# numbers = [1,2,3,4]
# biggest = numbers[0]
# for num in numbers:
#     if num > biggest:
#         biggest = num
# print(biggest)

#count a vowel 

sentence = "hello world Mani is HeRe"
vowels = "aeiou"
count = 0 
found = ""
for letter in sentence:
    if letter.lower() in vowels:
        count = count + 1
        found += letter
        

print(count)
print(found)