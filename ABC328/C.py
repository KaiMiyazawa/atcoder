N, Q = map(int, input().split())
S = input()
lr = [map(int, input().split()) for _ in range(Q)]
l, r = [list(i) for i in zip(*lr)]

SLIST = list(S)

# 連続する同じ文字のペアを事前に数えておく
pair_count = [0]
for i in range(1, N):
    pair_count.append(pair_count[-1] + (SLIST[i-1] == SLIST[i]))

for j in range(Q):
    result = pair_count[r[j] - 1] - pair_count[l[j] - 1]
    print(result)
