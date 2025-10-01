def hcf(a,b):
    while b:
        a,b = b, a%b
    return a 

def lcm (a,b):
    return (a*b) // hcf(a,b)

num1 = int(input())
num2 = int(input())
print("Lcm is :",lcm(num1,num2))