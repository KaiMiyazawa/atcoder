N = int(input())
A = list(map(int, input().split()))
SORT = sorted(A)
MIN = min(A)
MAX = max(A)
ORIGIN = range
j = 0;
for i in range(MIN, MAX):
  if not i == SORT[j]:
    print(SORT[j] - 1)
    break
  j+=1
