# input = "madam"

# result = ""

# for letter in input:
#     result = letter + result


# print(result)

# input = [5,8,2,10]

# bigg = input[0]
# for num in input:
#     if bigg < num:
#         bigg = num 

# print(bigg)


# input = "Python"
# vowel = "aeiou"

# input = input.lower()
# count = 0
# for i in input:
#     for j in vowel:
#         if i == j:
#             count += 1

# print(count)


# def palin():
#     result = ""
#     for l in input:
#         result = l + result
#     if result == input:
#         print("TRUE")
#     else:
#         print("FALSE")

# palin()


# input = [1,1,22,2,3,3,4]
# def rever():
#     res = []
#     for num in input:
#         if num not in res:
#             res.append(num)

#     print(res)

# rever()

# def prime():
#     num = int(input())
#     for i in range(2,num):
#         if num % i == 0:
#             print("Not")
#             break
#         else:
#             print("prime")
# prime()


# def sumof(num):
 
#     total = 0
#     while num > 0:
#         digit = num % 10
#         total = total +   digit
#         num  = num //10
#     return total 

# print(sumof(123))

#recursive method in factorial 
# def fact(n):
#     if n == 0 or n == 1:
#         return 1 
#     return n * fact(n-1)
# print(fact(5))

# def fact(n):
#     result = 1
#     for i in range(1,n+1):
#         result= result * i 
#     return result 
# print(fact(5))


