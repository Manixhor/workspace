n = "anaddd"


result = ""

for letter in n:
    # if letter in n:
        result = letter + result 
if result == n:
    print("it is a palindrome")
else:
    print("It is not a palindrome")