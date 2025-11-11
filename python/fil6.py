# li = [1,2,3,4]
# ans = 0

# for i in range(len(li)):
#     ans = ans + li[i]

# print(ans)


string = "abcd"
ans = 0
   
for i in range(len(string)-1):
    a = ord(string[i])
    b = ord(string[i+1])
    temp = abs(a-b)
    print(temp)
    ans = ans + temp

print(ans)
    
