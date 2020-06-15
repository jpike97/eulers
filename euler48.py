result = 0
for i in range(1, 1001):
	result = result + i**i

print(result % 10000000000)
