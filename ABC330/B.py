N, L, R = map(int, input().split())
A = list(map(int, input().split()))

RESULT = [0] * N
for i in range(N):
	if (A[i] < L):
		RESULT[i] = L
	elif (A[i] > R):
		RESULT[i] = R
	else:
		RESULT[i] = A[i]
print(*RESULT)
