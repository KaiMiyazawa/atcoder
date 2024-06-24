S = input()

N = len(S)

up = 0
lw = 0

for i in range(N):
  if S[i].isupper():
    up += 1
  if S[i].islower():
    lw += 1

if up > lw:
  print(S.upper())
else:
  print(S.lower())