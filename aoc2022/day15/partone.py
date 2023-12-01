lines = []
debug = 0
LINE = 10 if debug else 2000000

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
    for i in list(range(budget - abs(LINE - sy) + 1)):
        if (sx - i, LINE) not in beacons: cannot.add((sx - i, LINE))
        if (sx + i, LINE) not in beacons: cannot.add((sx + i, LINE))

print(len(cannot))