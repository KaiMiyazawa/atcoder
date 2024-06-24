N, K = map(int, input().split())
A = list(map(int, input().split()))

result = 0
tmp = K

for a in A:
  if tmp >= a:
    tmp -= a
  else:
    result += 1
    tmp = K - a

print(result+1)