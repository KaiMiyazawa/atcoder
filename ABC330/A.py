N, L = input().split()
A = list(map(int, input().split()))

result = 0
for i in range(int(N)):
	if (A[i] >= int(L)):
		result += 1
print(result)
