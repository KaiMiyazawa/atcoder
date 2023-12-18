M, D = map(int, input().split())
y, m, d = map(int, input().split())

if d == D:
    d = 1
    m = m + 1
else:
    d = d + 1

if m == M + 1:
    m = 1
    y = y + 1

print(y, m, d, sep=' ')
    
