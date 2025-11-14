li = [1,2,3,4]


def bigg():
    biggest = li[0]
    for num in li:
        if num > biggest:
            biggest = num
    return(biggest)

print(bigg())

# print(li)