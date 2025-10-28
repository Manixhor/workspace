nested = [[1,2],[3,4],[5,6]]

flat = []

for sublist in nested:
    for num in sublist:
        flat.append(num)
print(flat)