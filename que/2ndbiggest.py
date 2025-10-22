n = int(input())
arr = list(map(int, input().split()))		
result = []
for i in range(n):
	biggest = n[0]
	if i > biggest:	
		biggest = i
print(biggest)