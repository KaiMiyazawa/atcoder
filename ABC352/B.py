S = input()
T = list(input())

i = 0
for j, c in enumerate(T):
  if c == S[i]:
    i += 1
    print(j+1, end=" ")



