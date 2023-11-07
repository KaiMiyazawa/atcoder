B = int(input())

for i in range(1,16):
  if B == i**i:
    print(i)
    exit(0)
print(-1)
