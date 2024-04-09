N = int(input())
A = list(map(int, input().split()))

for i in range(N-1):
    x, y = map(int, input().split())
    tmp = A[i]//x
    A[i] -= x*tmp
    A[i + 1] += y*tmp
    
print(A[N-1])
