N = int(input())

matrix = [['#' for _ in range(3**N)] for _ in range(3**N)]


for n_tmp in range(N):
  n = n_tmp + 1
  if n == 1:
    for i in range(3**N):
      for j in range(3**N):
        if i%3 == 1 and j%3 == 1:
          matrix[i][j] = '.'
  else:
    for i in range(3**N):
      for j in range(3**N):
        if i//(3**n_tmp)%3 == 1 and j//(3**n_tmp)%3 == 1:
          matrix[i][j] = '.'



for row in matrix:
    print(''.join(row))