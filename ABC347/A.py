N, K = input().split()
A = list(map(int, input().split()))
N = int(N)
K = int(K)
for i in range(N):
  if A[i] % K == 0:
    print(int(A[i]/K), end=" ")
