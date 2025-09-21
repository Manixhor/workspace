number = [2,3,4,5]
largest = number[0]
for i in number:
    if i > largest:
        largest = i

print(largest)

sec_lar = number[0]

for i in number:
    if largest != i & i > sec_lar:
        sec_lar = i
print(sec_lar)