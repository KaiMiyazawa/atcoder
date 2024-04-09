# N = int(input())
# l = [list(map(int, input().split())) for l in range(N)]

import math

# 入力の受け取り
N = int(input())
points = []
for i in range(N):
    x, y = map(int, input().split())
    points.append((x, y))
    
max_distances = [0] * N
farthest_points = [0] * N
for i in range(N):
    max_dist = 0
    farthest_point = 0
    for j in range(N):
        if i != j:
            dist = math.sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)
            if dist > max_dist:
                max_dist = dist
                farthest_point = j+1
    max_distances[i] = max_dist
    farthest_points[i] = farthest_point

# 結果の出力
for i in range(N):
    print(farthest_points[i])
