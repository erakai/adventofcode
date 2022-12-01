class Node:
    def __init__(self, risk):
        self.risk = risk
        self.neighbors = [] 

    def __str__(self):
        return str(self.risk)

lines = open('day15/input.txt').read().splitlines()
lines = [[Node(int(y)) for y in x.strip()] for x in lines]

start, end = None, None
nodes = sum(lines, [])

for r in range(len(lines)):
    for c in range(len(lines[r])):
        if r == 0 and c == 0: start = lines[r][c]
        if r == len(lines) - 1 and c == len(lines[r]) - 1: end = lines[r][c]
        if r < len(lines) - 1: lines[r][c].neighbors.append(lines[r+1][c]) 
        if c < len(lines[r]) - 1: lines[r][c].neighbors.append(lines[r][c+1])
        if c > 0: lines[r][c].neighbors.append(lines[r][c-1]) 
        if r > 0: lines[r][c].neighbors.append(lines[r-1][c])

costs = {}
path = {}
smallest_risk_level = []
visit = [] 

costs[start] = 0
visit.append((0, start))
while len(visit) > 0:
    max_tup = min(visit, key = (lambda t: t[0]))
    current = max_tup[1]
    visit.remove(max_tup)

    if current == end: break

    for ne in current.neighbors:
        cost = costs[current] + ne.risk
        if ne not in costs.keys() or cost < costs[ne]:
            costs[ne] = cost 
            path[ne] = current 
            visit.append((cost, ne))

print('Sum:', costs[end])