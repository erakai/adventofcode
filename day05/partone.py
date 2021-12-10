lines = []
with open('day5/input.txt') as file:
    lines = file.readlines()

map = [] 
for i in range(1000):
    map.append([0] * 1000)

for line in lines:
    tokens = line.split(",")
    x1 = int(tokens[0])
    y1 = int(tokens[1].split()[0])
    x2 = int(tokens[1].split()[2])
    y2 = int(tokens[2])

    if (y1 == y2):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            map[x][y1] += 1
    if (x1 == x2):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            map[x1][y] += 1

total = 0
for row in map:
    for vent in row:
        if (vent > 1): total += 1 

print(total)