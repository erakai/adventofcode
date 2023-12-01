sum = 0
for x in range(4000000):
    if x % 100000 == 0: print(x)
    for y in range(4000000):
        if x > 50 and y > 50 and x < 100 and y < 100:
            sum += 1

print('Completed!')