import itertools

l = [1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111, 1111111111, 11111111111, 111111111111]

h = list(itertools.combinations_with_replacement(l,3))

k = []
for i in range(len(h)):
  k.append(h[i][0] + h[i][1] + h[i][2])
k.sort()
N = int(input())
print(k[N - 1])
