list1 = [1,2,3,4,3]

result = []

for i in list1:
    if i not in result:
        result.append(i)

print(result)

