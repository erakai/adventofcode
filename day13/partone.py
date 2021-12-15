lines = []
with open('day13/input.txt') as file:
    lines = file.readlines()

points = [tuple(map(int, x.split(","))) for x in lines if ',' in x]
directions = [x.strip().split(" ")[2] for x in lines[len(points) + 1:]]

grid = {}
max_val = 0
for point in points: max_val = max(max_val, point[0], point[1])
for i in range(max_val + 1):
    for j in range(max_val + 1):
        if (i, j) in points: grid[(i, j)] = 'x'

direction = directions[0]
is_x = direction[0] == 'x'
over = int(str(direction[2:]))
for i in range(max_val):
    for j in range(max_val):
        val = 'o'
        if (i, j) in grid.keys(): val = grid[(i, j)]
        if val != 'o':
            if not is_x:
                if j > over:
                    grid[(i, j - (2 * (j - over)))] = 'x'
                    grid[(i, j)] = 'o'
            else:
                if i > over:
                    grid[(i - 2 * (i - over), j)] = 'x'
                    grid[(i, j)] = 'o'


total = 0
for pos, val in grid.items():
    if val == 'x': total += 1 
print(total)