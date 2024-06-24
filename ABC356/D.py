def solve_efficient(N, M):
    MOD = 998244353
    total = 0
    for j in range(60):  # 0 <= M < 2^60 なので、最大で60ビットまで考慮
        if (M & (1 << j) == (1 << j)):
            num_times = (N + 1) // (1 << (j + 1)) * (1 << j)
            remainder = (N + 1) % (1 << (j + 1))
            if remainder > (1 << j):
                num_times += remainder - (1 << j)

            total = (total + num_times) % MOD

    return total

# 入力
N, M = map(int, input().split())
# 結果の出力
print(solve_efficient(N, M))
