# word1 = "listen"
# word2 = "silent"

# if len(word1) != len(word2):
#     print("not anagram")
# else:
#     is_anagram = True
#     letters = list(word2)
#     for letter in word1:
#         if letter in letters:
#             letters.remove(letter)
#         else:
#             is_anagram = False
#             break
    
#     print(is_anagram)

# rows = 4

# for i in range(1,rows + 1):
#     print("*"* i)

# txt = "banana"

# freq = {}
# for char in txt:
#     if char not in freq:
#         freq[char] = 0
#     freq[char] += 1

# for key in freq:
#     print(key,":",freq[key])

# nested = [[1,2],[3,4]]
# flat = []
# for sublist in nested:
#     for item in sublist:
#         flat.append(item)
# print(flat)

# num = [0,1,2,3,3]

# result = []

# for x in num:
#     if x != 0:
#         result.append(x)
# for x in num:
#     if x == 0:
#         result.append(x)
# print(result)

# s = "(()())"
# stack = []
# balanced = True
# for ch in s:
#     if ch == '(':
#         stack.append(ch)
#     else:
#         if not stack:
#             balanced = False
#             break
#         stack.pop()
# if balanced and not stack:
#     print("balanced")
# else:
#     print("not balanced")


# nums = [1,2,3,4,5]
# k = 2
# k = k%len(nums)
# rotated = nums[-k:] + nums[:-k]
# print(rotated)

nums = [2,7,11,5]
target = 9

seen = set()
for n in nums:
    need = target -n 
    if need in seen:
        print((need,n))
        break
    seen.add(n)