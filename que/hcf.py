def hcf(a,b):
    while b: 
        a, b = b, a%b
    return a 
num1 = int(input())
num2 = int(input())

print("HCF is: ",hcf(num1,num2))