N, Q = map(int, input().split())
T = list(map(int, input().split()))

teeth = [0]*N

for i in range(Q):
  if teeth[T[i]-1] == 0:
    teeth[T[i]-1] = 1
  else:
    teeth[T[i]-1] = 0

result = 0
for j in range(N):
  if teeth[j] == 1:
    result += 1
print(N - result)
