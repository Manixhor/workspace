l1 = "apple"
l2 = "grapes"

common = []

for letter in l1:
    for le in l2:
        if le == letter:
            common.append(le)

print(set(common))