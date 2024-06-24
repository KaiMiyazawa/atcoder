def calculate_A(N):
    MOD = 998244353
    if N == 0:
        return 0
    K = len(str(N))  # Nの桁数を求める

    # 10^K - 1 とその逆元を求める
    divisor = pow(10, K, MOD) - 1
    inv_divisor = pow(divisor, MOD - 2, MOD)  # フェルマーの小定理を使用して逆元を求める

    # 10^(N*K) - 1 を計算する
    exponent = N * K
    numerator = pow(10, exponent, MOD) - 1

    # Aを計算する
    A = N * (numerator * inv_divisor % MOD) % MOD
    return A

# 例として N = 123456789012345678 を計算してみる
N = int(input())
result = calculate_A(N)
print(result)
