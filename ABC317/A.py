N, H, X = map(int, input().split())
P = list(map(int, input().split()))
for count in range(0, N):
  if H + P[count] >= X:
    print(count + 1)
    break
