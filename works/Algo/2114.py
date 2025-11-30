li = ["hello a good","bad","great work"]

ans = 0 
for j in range(len(li)):
    s = li[j]
    temp = 1
    for i in range(len(s)):
        ch = s[i]
        if ch == " ":
            temp = temp + 1
    ans = max(ans, temp)

print(ans)