
list2 = input("enter with spaces")

ch = list2.split()
#ist1 = [1,2,3,4,3]

result = []
#this i in ch iterates every element that entered in input 
for i in ch:
    if i not in result:
        result.append(i)

print(result)

