H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
result = 0

for i in range(H):
	for j in range(W):
		if A[i][j] == '#' or A[i][j] == 'd':
			if j != W - 1 and A[i][j + 1] == '#':
				A[i][j + 1] = 'd'
			if i != H - 1:
				if j != 0 and A[i + 1][j - 1] == '#':
					A[i + 1][j - 1] = 'd'
				if A[i + 1][j] == '#':
					A[i + 1][j] = 'd'
				if j != W - 1 and A[i + 1][j + 1] == '#':
					A[i + 1][j + 1] = 'd'
			if A[i][j] == '#':
				A[i][j] = 'd'
				result = result + 1
				if i != H and j != 0 and A[i + 1][j - 1] == 'd':
					result = result - 1
print(result)