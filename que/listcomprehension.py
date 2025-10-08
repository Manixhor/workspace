num = [1,2,3,4,5,6,7]
evens = [n for n in num if n%2==0]
squaredodds = [n**2 for n in num if n%2 != 0]
div_tuples = [(n,n**2) for n in num if n%3 == 0  ]

print(evens)
print(squaredodds)
print(div_tuples)
