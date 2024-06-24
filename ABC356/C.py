import itertools as itr

N, M, K = map(int, input().split())

tmp = [list(input().split()) for l in range(M)]

R = []
for i, l in enumerate(tmp):
  R.append(l[-1])
  tmp[i] = tmp[i][:-1]

C = []
for i, l in enumerate(tmp):
  C.append(l[0])
  tmp[i] = tmp[i][1:]

A = tmp

# ==========

def generate_bitmasks(N):
    # 0 から 2^N - 1 までの全ての数値を生成
    return range(2**N)

def get_bitmasks(N):
  bitmasks = generate_bitmasks(N)
  result = []
  for mask in bitmasks:
    result.append(f'{mask:0{N+1}b}')
  return result

bits = get_bitmasks(N)

# print(bits)
# print(A)
result = 0
for bit in bits:
  c_key = bit.count('1')
  flag = True
  bit = list(bit)
  for i, Arow in enumerate(A):
    Icount = 0
    for a in Arow:
      if bit[int(a)] == '1':
        Icount += 1

    if R[i] == 'o':
      if Icount >= K:
        continue
      else:
        flag = False
        break
    elif R[i] == 'x':
      if Icount < K:
        continue
      else:
        flag = False
        break
  if flag:
    result += 1
print(result)
