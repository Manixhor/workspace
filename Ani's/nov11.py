li = ["--X","X++","X--"]
x = 0 
for i in li:
    if i == "--X" or "X--":
        x = x - 1
    else:
        x = x + 1

print(x)