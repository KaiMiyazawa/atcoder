N, M, P = map(int, input().split())
result = 0;
#i -> 1からNまで
for i in range(N):
  if (i + 1 == M + (result) * P):
    result += 1
print(result)
