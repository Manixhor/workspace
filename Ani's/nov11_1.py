# n = "1.1.1.1"

# n1 = n.replace(".","[.]")
# print(n1)

# ans = ""
# for i in n:
#     ch = i
#     if ch == ".":
#         ans = ans + "[.]"
#     else:
#         ans = ans + ch
# print(ans)

stones = "abbBBB"
jewels = "ab"
ans = 0
for i in range(len(jewels)):
    for j in range(len(stones)):
        chi = jewels[i]
        chj = stones[j]
        if chi == chj:
            ans = ans + 1
print(ans)

