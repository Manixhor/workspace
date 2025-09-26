num = int(input("enter your number: "))

a = 0 
b = 1
for i in range(1,num):
    c = a + b
    print(f"{a} + {b} = {c} ")
    a = b 
    b = c 