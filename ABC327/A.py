N = int(input())
S = input()

if (S.find('ab') != -1):
  print('Yes')
elif (S.find('ba') != -1):
  print('Yes')
else:
  print('No')
