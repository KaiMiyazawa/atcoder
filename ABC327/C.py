def box(row, line):
  BOX_ARR = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  for i in range(row - 3, row):
    for j in range(line - 3, line):
      tmp = num_list[i][j] - 1
      if (BOX_ARR[tmp] != -1):
        BOX_ARR[tmp] = -1
      else:
        print('No')
        exit(0)

num_list = []
for i in range(9):
    num_list.append(list(map(int,input().split())))

ARR = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(9):
  ARR = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  for j in range(9):
    tmp = num_list[i][j] - 1
    if (ARR[tmp] != -1):
      ARR[tmp] = -1
    else:
      print('No')
      exit(0)

for i in range(9):
  ARR = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  for j in range(9):
    tmp = num_list[j][i] - 1
    if (ARR[tmp] != -1):
      ARR[tmp] = -1
    else:
      print('No')
      exit(0)

box(3, 3)
box(3, 6)
box(3, 9)
box(6, 3)
box(6, 6)
box(6, 9)
box(9, 3)
box(9, 6)
box(9, 9)

print('Yes')
