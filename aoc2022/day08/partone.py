lines = []
debug = 0

# there is a much more efficient dp solution that i could probaly write in like 5 min but i dont want to 
# so i will just copy paste my beautiful functions

with open('test.txt' if debug else 'input.txt') as file:
    lines = file.readlines()

grid = [[int(x) for x in y.strip()] for y in lines]

def tree(x, y):
    return grid[x][y]

def left(x, y):
    given = tree(x, y)
    while y > 0:
        y -= 1
        if given <= tree(x, y): return False
    return True

def right(x, y):
    given = tree(x, y)
    while y < len(grid[0]) - 1:
        y += 1
        if given <= tree(x, y): return False
    return True

def down(x, y):
    given = tree(x, y)
    while x < len(grid) - 1:
        x += 1
        if given <= tree(x, y): return False
    return True

def up(x, y):
    given = tree(x, y)
    while x > 0:
        x -= 1
        if given <= tree(x, y): return False
    return True

visible =  0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if up(x, y) or down(x, y) or right(x, y) or left(x, y): 
            visible += 1

print(visible)




