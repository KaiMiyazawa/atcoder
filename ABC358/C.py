from itertools import combinations

def min_stalls_to_visit(N, M, S):
    all_flavors = set(range(M))
    stalls = []
    for s in S:
        flavors = set()
        for i, char in enumerate(s):
            if char == 'o':
                flavors.add(i)
        stalls.append(flavors)
    min_stalls = N
    for r in range(1, N + 1):
        for comb in combinations(stalls, r):
            covered_flavors = set()
            for stall in comb:
                covered_flavors.update(stall)
            if covered_flavors == all_flavors:
                min_stalls = r
                return min_stalls

    return min_stalls

N, M = map(int, input().split())
S = [input().strip() for _ in range(N)]

result = min_stalls_to_visit(N, M, S)
print(result)
