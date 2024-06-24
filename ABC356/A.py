N, L, R = map(int, input().split())

a = list(range(1, L))
b = list(range(R, L-1, -1))
c = list(range(R+1, N+1))

# print(a+b+c)
d = a+b+c

for i in d:
  print(i, end=" ")