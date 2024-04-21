S = input()

S = list(S)

num = S[3:]

result = int(''.join(num))
if result == 316:
  print('No')
elif result < 1 or result >= 350:
  print('No')
else:
  print('Yes')
