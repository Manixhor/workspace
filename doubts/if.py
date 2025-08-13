m = int(input())

n = m%2
if n !=0:
    print("Weird")
if 6 >= n <= 20:
    print("Weird")
elif 2 >= n <= 5 or n > 20:
    print("Not weird")
