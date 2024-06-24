N, M = map(int, input().split())
H = list(map(int, input().split()))

result = 0
for i in range(N):
  M -= H[i]
  if M >= 0:
    result += 1
print(result)