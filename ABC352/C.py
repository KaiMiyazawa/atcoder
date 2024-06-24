N = int(input())
ab = [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*ab)]

i = 0
i_max = 0
v_max = B[0] - A[0]
for a, b in zip(A, B):
  if v_max < b - a:
    v_max = b - a
    i_max = i
  i += 1

# # print(C)
# print(i_max)
# print(v_max)

result = 0
i = 0
for a, b in zip(A, B):
  if i == i_max:
    result += b
  else:
    result += a
  i += 1
print(result)