N, X, Y, Z = map(int, input().split())

flag = False
if X < Y:
  l = range(X, Y)
else:
  l = range(Y, X)

for i in l:
  if i == Z:
    print("Yes")
    flag = True
if flag == False:
  print("No")