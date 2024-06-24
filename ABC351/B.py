N = int(input())
A = [list(input()) for l in range(N)]
B = [list(input()) for l in range(N)]

for i in range(N):
  for j in range(N):
    if A[i][j] != B[i][j]:
      print(int(i)+1, int(j)+1)