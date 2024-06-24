N= int(input())
A = list(map(int, input().split()))
rsA = sorted(A, reverse=True)

def count_pairs_exceeding_sum(lst, target_sum=10**8):
    lst.sort()
    left, right = 0, len(lst) - 1
    count = 0

    while left < right:
        if lst[left] + lst[right] > target_sum:
            count += (right - left)
            right -= 1
        else:
            left += 1

    return count

over_count = count_pairs_exceeding_sum(A)
# print(over_count)
result = sum(A)
result *= N-1
result -= over_count*(10**8)

print(result)