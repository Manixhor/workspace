
list1 = [1,2,3,1,2,2]

result = []
for i in list1:
    if i not in result:
        result.append(i)

print(result)