# 入力の受け取り
N = int(input())
beans = []
for i in range(N):
    a, c = map(int, input().split())
    beans.append((a, c))

kind = {}

for a, c in beans:
  if (c not in kind) or (kind[c] > a):
    kind[c] = a

print(max(kind.values()))
