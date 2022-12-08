lines = []
debug = 0

with open('test.txt' if debug else 'input.txt') as file:
    lines = file.readlines()

grid = [[int(x) for x in y.strip()] for y in lines]

def tree(x, y):
    return grid[x][y]

def left(x, y):
    given = tree(x, y)
    count = 0
    while y > 0:
        y -= 1
        count += 1
        if given <= tree(x, y): break 
    return count

def right(x, y):
    given = tree(x, y)
    count = 0
    while y < len(grid[0]) - 1:
        y += 1
        count += 1
        if given <= tree(x, y): break 
    return count

def down(x, y):
    given = tree(x, y)
    count = 0
    while x < len(grid) - 1:
        x += 1
        count += 1
        if given <= tree(x, y): break
    return count

def up(x, y):
    given = tree(x, y)
    count = 0
    while x > 0:
        x -= 1
        count += 1
        if given <= tree(x, y): break
    return count

visible =  0
scores = []
for x in range(len(grid)):
    for y in range(len(grid[0])):
        scores.append(up(x, y) * down(x, y) * right(x, y) * left(x, y))

print(max(scores))




