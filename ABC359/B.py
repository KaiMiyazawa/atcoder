N = int(input())
A = list(map(int, input().split()))

result = 0
for i in range(1, N+1):

  for j in range(2*N):
    if i == A[j]:
      if j+2 < 2*N and i == A[j+2]:
        result += 1
      else:
        break
print(result)