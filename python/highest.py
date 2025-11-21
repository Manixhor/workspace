rakhi = [5,8,10,11,50,15,20,25]

big = rakhi[0]
for num in rakhi:

    if num > big:
        big = num

print(big)

print(min(rakhi))
print(max(rakhi))


# ans = 0
# for i in range(len(rakhi)):
#     val = rakhi[i]
#     if val > ans:
#         ans = val
# print(ans)