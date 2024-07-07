A = list(map(int, input().split()))
B = list(map(int, input().split()))

if A[3] > B[0] and A[4] > B[1] and A[5] > B[2] and A[0] < B[3] and A[1] < B[4] and A[2] < B[5]:
  print("Yes")
else:
  print("No")
