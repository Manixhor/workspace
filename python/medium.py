
# d1 = {"a":1}
# d2 = {"b":2}

# d3 = d1 | d2
# print(d3)


# input1 = [1,2,3,4]
# input2 = [1,2,3]
# c = []
# for i in input1:
#     if i in input2:
#         c.append(i)
# a= set(input1)
# b = set(input2)
# c = a & b
# print(c)



l1 = [1,2,2,3]
def occ():
    result = []
    for num in l1:
        if num not in result:
            result.append(num)

    print(result)
occ()