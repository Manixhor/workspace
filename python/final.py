
li1 = [1,2,3,4]
bigg = li1[0]

bigg2 = li1[0]


for num in li1:
    if num > bigg:
        bigg = num

for num1 in li1:
    if num1  > bigg2 and num1 != bigg:
        bigg2 = num1
print(bigg2)
