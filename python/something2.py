#list comprehension 
# num = [i*2 for i in range(5)]
# print(num)

# num1 = [i for i in range(10) if i % 2 == 0]
# print(num1)


num = [12,3,12,22,14]
freq = {}
for i in num:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)