S = input()
flag = False
for i in range(3):
  if S[i] == 'R' and flag == False:
    print("Yes")
  elif S[i] == 'R' and flag == True:
    print("No")
  if S[i] == 'M':
    flag = True
