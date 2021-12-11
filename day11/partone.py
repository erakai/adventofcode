lines = []
with open('day11/input.txt') as file:
    lines = file.readlines()

total = [0]
def check_flash(r, c, grid, start=False):
    if r >= len(grid) or c >= len(grid[r]) or r < 0 or c < 0: return
    if not start: grid[r][c] += 1
    if (grid[r][c] > 9):
        total[0] += 1
        grid[r][c] = -10000
        check_flash(r - 1, c, grid)
        check_flash(r + 1, c, grid)
        check_flash(r, c - 1, grid)
        check_flash(r, c + 1, grid)
        check_flash(r - 1, c - 1, grid)
        check_flash(r - 1, c + 1, grid)
        check_flash(r + 1, c - 1, grid)
        check_flash(r + 1, c + 1, grid)

grid = [[int(i) for i in list(x.strip())] for x in lines]

for i in range(100):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            grid[r][c] += 1
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            check_flash(r, c, grid, start=True)
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] < 0: grid[r][c] = 0

print(total[0])