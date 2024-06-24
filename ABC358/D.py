N, M = map(int, input().split())
A_o = list(map(int, input().split()))
B_o = list(map(int, input().split()))

A = sorted(A_o)
B = sorted(B_o)

result = 0

i = 0
for a in A:
  if i == M:
    break
  b = B[i]
  if b <= a:
    result += a
    i += 1
if i < M:
  print(-1)
else:
  print(result)
