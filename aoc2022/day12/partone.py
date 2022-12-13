import heapq
import random

lines = []
debug = 0

with open('test.txt' if debug else 'input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

grid = []
end = ()
start = ()
for row, line in enumerate(lines):
    grid.append([])
    for col, char in enumerate(line):
        if char == 'E': 
            grid[row].append(26)
            end = (row, col)
        elif char == 'S':
            grid[row].append(1)
            start = (row, col)
        else:
            grid[row].append(ord(char) - 96)


def neighbors(grid, pos):
    n = []
    if pos[0] < len(grid) - 1: n.append((pos[0] + 1, pos[1]))
    if pos[1] < len(grid[0]) - 1: n.append((pos[0], pos[1] + 1))
    if pos[0] > 0: n.append((pos[0] - 1, pos[1]))
    if pos[1] > 0: n.append((pos[0], pos[1] - 1))
    return n

def valid(grid, c, n):
    return grid[c[0]][c[1]] - grid[n[0]][n[1]] >= -1 

def weight(grid, c, n):
    return 1

def dijkstra(grid, start):
    dist = {}
    prev = {}
    q = []
    vi = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) != start:
                dist[(i, j)] = 100000
                prev[(i, j)] = (-1, -1)
                heapq.heappush(q, (100000, (i, j)))

    dist[start] = 0
    prev[start] = (-1, -1)
    heapq.heappush(q, (0, start))

    while len(q) > 0:
        tup = heapq.heappop(q)
        c = tup[1]
        vi.append(c)

        for n in neighbors(grid, c):
            if n not in vi and valid(grid, c, n):
                d = dist[c] + weight(grid, c, n)
                if d < dist[n]:
                    q.remove((dist[n], n))
                    heapq.heappush(q, (d, n))
                    heapq.heapify(q)
                    dist[n] = d
                    prev[n] = c

    return (dist, prev)

tree = dijkstra(grid, start)
print('From', start, 'to', end)
print(tree[0][end])