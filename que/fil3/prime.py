n = int(input("enter your number: "))

if n < 2:
    print("it's not a prime")
else:
    is_prime = True 
    for i in range (2,n):
        if n % 2 == 0:
            is_prime = False
            break
    if is_prime:
        print("its a prime")
    else:
        print("not a prime number")