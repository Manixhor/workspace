li = ["--X","X++"]
X = 0 
for i in li:
    #temp = i 
    if i == "--X" or i == "X--":
        X = X -1
    else:
        X = X + 1
print(X)
