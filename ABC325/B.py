N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

max_num = 0
time = 0

for i in range(24):
	num = 0
	for j in range(N):
		time = A[j][1] + i
		if time >= 24:
			time = time - 24
		if time > 9 and time <= 18:
			num = num + A[j][0]
	if num > max_num:
		max_num = num

print(max_num)