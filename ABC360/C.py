N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

l = [[] for _ in range(N+2)]
for i in range(N):
  l[A[i]].append(W[i])
  
# for i in range(N):
#   print(l[i])

result = 0
for i in l:
  if len(i) >= 2:
    result += sum(i) - max(i)
print(result)
# dups = [i for i, x in enumerate(l) if x>=2]

# result = 0
# for i in dups:
#   L = list()
#   ind = [j for j, x in enumerate(A) if x==i]
#   for j in ind:
#     L.append(W[j])
#   L.remove(max(L))
#   result += sum(L)
# print(result)
