def fib():
    total = 0 
    a = 1
    b = 2
    while a < 400000:
        if a % 2 == 0:
            total += a
        a,b = b, a+b 
    return total

print(fib())
#even fibonnaci 
