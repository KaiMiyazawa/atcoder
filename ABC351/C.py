N = int(input())
A = list(map(int, input().split()))

l = []
for i in range(N):
  l.append(A[i])
  if len(l) <= 1:
    continue
  if l[-1] != l[-2]:
    continue
  while (l[-1] == l[-2]):
    l[-2] += 1
    l.pop(-1)
    if len(l) <= 1:
      break

print(len(l))