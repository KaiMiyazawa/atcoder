N, M = map(int, input().split())
A = list(map(int, input().split()))
X = [list(map(int, input().split())) for l in range(N)]

R = [0] * (M+1)

for i in range(N):
  for j in range(M):
    R[j] += X[i][j]

for r, a in zip(R, A):
  if r < a:
    print("No")
    exit()

print("Yes")