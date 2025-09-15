n = int(input())

if n < 2:
    print("not a prime number")

else:
    is_prime = True
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
            
            break 
    if is_prime:
        print("prime")
    else:
        print("not a prime number")