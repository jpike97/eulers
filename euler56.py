highest = 0

def checkDigitSum(number):
    global highest
    sum = 0
    for x in str(number):
        sum = sum + int(x)
    if sum > highest:
        highest = sum
for a in range(99, 90, -1):
    for b in range(99, 90, -1):
        checkDigitSum(a**b)

print(highest)