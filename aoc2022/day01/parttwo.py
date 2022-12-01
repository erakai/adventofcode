lines = []

with open('input.txt') as file:
    lines = file.readlines()

max = 0
max2 = 0
max3 = 0
current = 0

for line in lines:
    if len(line.strip()) == 0:
        if current > max:
            max3 = max2
            max2 = max
            max = current
        elif current > max2:
            max3 = max2
            max2 = current
        elif current > max3:
            max3 = current
        current = 0
    else:
        current = current + int(line)

print(max + max2 + max3)
