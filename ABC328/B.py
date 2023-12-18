N = int(input())
D = list(map(int, input().split()))

result = 0
for i in range(1, N+1):
    for j in range(1, D[i - 1] + 1):
        if j%11 == 0 and i == j:
            result = result + 1
        elif j == i/11:
            result = result + 1
        elif i == j/11:
            result = result + 1
        elif i < 10 and i == j:
            result = result + 1
print(result)
