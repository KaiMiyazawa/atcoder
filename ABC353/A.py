N = int(input())
H = list(map(int, input().split()))

result = -1

for i, a in enumerate(H):
  if i == 0:
    continue
  if H[0] < a:
    result = i+1
    break

print(result)