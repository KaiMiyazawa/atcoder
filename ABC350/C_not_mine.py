def solve(N, A):
    pos = [0] * (N + 1)  # pos[i] は値 i の位置を表す
    for i in range(N):
        pos[A[i]] = i + 1

    swaps = []
    for i in range(1, N + 1):
        while A[i - 1] != i:
            j = pos[i]  # 値 i の現在の位置
            A[i - 1], A[j - 1] = A[j - 1], A[i - 1]
            pos[A[j - 1]], pos[i] = pos[i], pos[A[j - 1]]  # pos の更新
            swaps.append((i, j))

    return swaps

# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))

# 操作を行い、操作と交換された要素のインデックスを取得
swaps = solve(N, A)

# 操作回数と操作内容を出力
print(len(swaps))
for swap in swaps:
    print(*swap)
