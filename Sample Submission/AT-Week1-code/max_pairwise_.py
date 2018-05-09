# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0
index_max1 = 0

for i in range(1,n):
	if a[i]>a[index_max1]:
		index_max1=i

a[n-1],a[index_max1] = a[index_max1],a[n-1]

index_max1 = 0

for i in range(1,n-1):
	if a[i]>a[index_max1]:
		index_max1=i
print(a[index_max1]*a[n-1])