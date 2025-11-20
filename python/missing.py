# num = [1,2,3,5,6]

# n = 6

# expected = n *(n+1)//2
# actual = sum(num)

# missing = expected - actual
# print(missing)



# def fact(n):
#     if n == 0 or n == 1:
#         return 1 
#     return n * fact(n-1)

# print(fact(2))

# text = "banana"

# freq = {}
# for char in text:
#     if char not in freq:
#         freq[char] = 0
#     freq[char] = freq[char] + 1

# for key in freq:
#     print(key,":",freq[key])


# file = open("he.txt","r")
# count = 0 
# for line in file:
#     count = count + 1

# file.close()
# print(count)

# def hanoi(n,source,helper,target):
#     if n == 1:
#         print("Move disk 1 from",source,"to",target)
#         return
#     hanoi(n-1,source,target,helper)
#     print("move disk",n,"from",source,"to",target)

#     hanoi(n-1,helper,source,target)
# hanoi(3,"A","B","C")


# num = [2,3,1,233,2]

# small = num[0]

# for s in num:
#     if s < small:
#         s = small
# print(small)