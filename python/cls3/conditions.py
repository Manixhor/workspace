# for upper in range(1,3):
#     print(upper)
n = 11
for x in range(2, n):
    if n % x == 0:
        print(n, "is not a prime number")
        print("First divisor is", x, "and quotient is", n // x)
        break
else:
    print(n, "is a prime number")
