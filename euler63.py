count = 0
for i in range(1,10):
    for j in range(1, 50):
        a = i**j
        if len(str(a)) == j:
            count += 1
print (count)