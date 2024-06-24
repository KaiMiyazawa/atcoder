N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = A + B
Cs = sorted(C)
As = sorted(A)

a = 0
found = False
for i in range(N+M):
    if Cs[i] == As[a]:
        if a+1 < N and Cs[i+1] == As[a+1]:
            print('Yes')
            found = True
            break
        a += 1
        if a >= N:  # Asのインデックスが範囲外にならないようにする
            break

if not found:
    print('No')
