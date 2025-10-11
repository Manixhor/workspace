import copy
original = [[1,2,3,4],[6,7,4,32,]]

shallow = copy.copy(original)

deep = copy.deepcopy(original)

original[0][0] = 99

print("original",original)
print("shallow",shallow)
print("deep",deep)