S = str(input())
A = set()

for i in range(len(S) + 1):
  for j in range(len(S) - i + 1):
    A.add(S[i:i+j])
A.discard("")

print(len(A))
