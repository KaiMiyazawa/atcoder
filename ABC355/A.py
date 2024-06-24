A, B, = map(int, input().split())

if A != B:
  l = [1, 2, 3]
  l.remove(A)
  l.remove(B)
  print(l[0])
else:
  print(-1)