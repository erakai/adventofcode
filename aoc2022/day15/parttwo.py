lines = []
debug = 0
LIMIT = 20 if debug else 4000000

with open('test.txt' if debug else 'input.txt') as file:
    lines = [x.strip() for x in file.readlines()]

sensors = {}
beacons = set()
cannot = set()

for line in lines:
    x1 = int(line[line.index('Sensor at x=')+12:line.index(',')])
    y1 = int(line[line.index(', y=')+4:line.index(':')])
    x2 = int(line[line.index('closest beacon is at x=')+23:line.index(',', line.index(',')+1)])
    y2 = int(line[line.index(', y=', line.index(',')+1)+4:])
    sensors[(x1, y1)] = abs(x2 - x1) + abs(y2 - y1)
    beacons.add((x2, y2))

for sx, sy in sensors:
    budget = sensors[(sx, sy)]
    for line in range(LIMIT + 1):
        for i in list(range(budget - abs(line - sy) + 1)):
            if (sx - i <= LIMIT and sx - i >= 0): cannot.add((sx - i, line))
            if (sx + i <= LIMIT and sx + i >= 0): cannot.add((sx + i, line))

for x in range(LIMIT):
    for y in range(LIMIT):
        if (x, y) not in cannot:
            print(x * 4000000 + y)

# iterate through each sensor
# add each sensor's blocking range to an array of shapes
# then iterate through every element in grid and check if in shapes? O(4sn^2) comparisons