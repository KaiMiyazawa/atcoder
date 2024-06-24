N, A = map(int, input().split())
T = list(map(int, input().split()))

time = 0
for t in T:
  if t >= time:
    print(t + A)
    time = t + A
  else:
    print(time + A)
    time = time + A
