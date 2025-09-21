number = [12,3,4,233,12]

#Let us assume 0th place is largest
largest = number[0]
for i in number:
    if i > largest:
        largest = i

print(largest)

second_largest = number[0]
for i in number:
    if i != largest and i > second_largest:
        second_largest = i
print(second_largest)        

