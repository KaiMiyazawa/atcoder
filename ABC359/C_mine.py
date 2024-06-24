sx, sy = map(int, input().split())
tx, ty = map(int, input().split())

yd = sy - ty
if yd < 0:
  yd = -yd

xd = sx - tx
if xd < 0:
  xd = -xd

xd = xd - yd
if xd < 0:
  xd = 0

if sy == ty:
  if sx == tx:
    print(0)
    exit()
  if sy%2 == 0:
    if sx < tx and sx%2 == 0 and tx-sx == 1:
      print(0)
      exit()
    elif tx < sx and tx%2 == 0 and sx-tx == 1:
      print(0)
      exit()
  else:
    if sx < tx and sx%2 == 1 and tx-sx == 1:
      print(0)
      exit()
    elif tx < sx and tx%2 == 1 and sx-tx == 1:
      print(0)
      exit()

result = 0

if sy == ty:
  if sx < tx:
    if sy%2 == 0 and xd%2 == 1 and sx%2 == 1:
      result += 1
    elif sy%2 == 1 and xd%2 == 1 and sx%2 == 0:
      result += 1
  else:
    if sy%2 == 0 and xd%2 == 1 and tx%2 == 1:
      result += 1
    elif sy%2 == 1 and xd%2 == 1 and tx%2 == 0:
      result += 1

result += yd + xd//2
print(result)