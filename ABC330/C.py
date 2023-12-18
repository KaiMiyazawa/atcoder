import math
D = int(input())
DS = int(math.sqrt(D))
result = D
for x in range(DS + 1):
	y = int(math.sqrt(D - x * x))
	ab = abs(x * x + y * y - D)
	if ab < result:
		result = ab
	y = y + 1
	ab = abs(x * x + y * y - D)
	if ab < result:
		result = ab
print(result)
