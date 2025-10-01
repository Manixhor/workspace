
def find_hcf(a,b):
    hcf = 1 
    for i in range(1,min(a,b) + 1):
        if a % i == 0 and b % i == 0:
            hcf = i
    return hcf

def find_lcm(a,b):
    hcf = find_hcf(a,b)
    lcm = (a*b) // hcf
    return lcm 

num1 = 8
num2 = 12 