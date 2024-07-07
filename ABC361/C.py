N, K = map(int, input().split())
A = list(map(int, input().split()))
# print("oA", A)
A.sort()

left = 0
right = N-1
# print(A[left:right+1])
for i in range(K):
  ldiff = A[left+K-i] - A[left]
  rdiff = A[right] - A[right-K+i]
  # print(ldiff, rdiff, i)
  if rdiff >= ldiff:
    right -= 1
  else:
    left += 1
  # print(A[left:right+1])
  
print(A[right] - A[left])
