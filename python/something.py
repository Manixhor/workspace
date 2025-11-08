
# char1 = "mani"
# vowels = "aeiou"
# def counting1():
#     count = 0 

#     for letter in char1:
#         if letter in vowels:
#             count += 1

#         else:
#             count = 1

#     print(count)
# counting1()




# a = "Mani"
# def rev():
#     result = ""

#     for letter in a:
#         result = letter + result

#     print(result)

#     if result == a: 
#         print("it is palindrome")
#     else:
#         print("not a palindrome")
# rev()

# list1 = [1,2,3,4,5,2,1]

# def secnd():
#     l = list1[0]
#     l1 = list1[0]
#     for num in list1:
#         if l < num:
#             l = num
#     for num in list1:
#         if num != l and l1 < num:
#             l1 = num
#     print(l1)
# secnd()


# li1 = [1,4,3,2,1]
# result = []
# def rev():

   
#     for num in li1:
#         if num not in result:
#             result.append(num)

#     print(result)

# rev()

# def flatten_list(nested_list):
#     result = []
#     for item in nested_list:
#         if isinstance(item,list):
#             result.extend(flatten_list(item))
#         else:
#             result.append(item)
#     return result

# print(flatten_list([1,[2,[3,4]],5]))

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
    
# print(fact(3))


# student = {
#     "name" : "Mani",
#     "age" : 23,
#     "grade": "S"
# }
# for key, value in student.items():
#     print(key,":",value)

# name = "mani"
# vowel = "aeiou"

# def rm():
#     result = []
#     for letter in name:
#        if letter not in vowel:
#            result += letter
#     print(result)

# rm()



word1 = "Listen".lower()
word12 = "silents".lower()
if len(word1) != len(word12):
    print("not anagram")
else:
    is_anagram = True
    letters = list(word12)
    for letter in word1:
        if letter in letters:
            letters.remove(letter)
        else:
            is_anagram = False
            break
    if is_anagram:
        print("yep")
    else:
        print("no it's not anagram")



