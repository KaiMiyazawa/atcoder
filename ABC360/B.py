S, T = input().split()
n = len(S)
for w in range(1, n):
  parts = [S[i:i + w] for i in range(0, n, w)]
  for c in range(1, w + 1):
    result = ''
    for part in parts:
      if len(part) >= c:
        result += part[c - 1]
    if result == T:
      print("Yes")
      exit()
print("No")
