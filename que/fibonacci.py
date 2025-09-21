n = int(input("how many times you have to print "))


#initial 
a = 0 
b = 1

for i in range(n):
    print(a)
    c = a + b 
    a = b 
    b = c 