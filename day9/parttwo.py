# Recursive function that takes in a point and a map and returns the number of nearby connections that "flow" towards it
graphed = [] # screaming emoji
def find_basin_size(map, row, col, start=None):
    if row < 0 or row > len(map) - 1 or col < 0 or col > len(map[row]) - 1:
        return 0
    if start:
        graphed.clear()
        return find_basin_size(map, row - 1, col) + \
                find_basin_size(map, row + 1, col) + \
                find_basin_size(map, row, col - 1) + \
                find_basin_size(map, row, col + 1) 

    size, val = (0 if [row, col] in graphed else 1), map[row][col]
    if val == 9: return 0 
    graphed.append([row, col])
    if row > 0 and [row - 1, col] not in graphed:
        size += find_basin_size(map, row - 1, col)
    if row < len(map) - 1 and [row + 1, col] not in graphed:
        size += find_basin_size(map, row + 1, col)
    if col > 0 and [row, col - 1] not in graphed:
        size += find_basin_size(map, row, col - 1)
    if col < len(map[row]) - 1 and [row, col + 1] not in graphed:
        size += find_basin_size(map, row, col + 1)
    return size

lines = []
with open('day9/input.txt') as file:
    lines = file.readlines()

map = [list(l.strip()) for l in lines]
map = [[int(c) for c in r] for r in map]

low_points = []
for row in range(len(map)):
    for col in range(len(map[row])):
        val = map[row][col]
        is_low_point =  (row == 0 or val < map[row-1][col]) and \
                        (row == len(map) - 1 or val < map[row+1][col] ) and \
                        (col == 0 or val < map[row][col-1]) and \
                        (col == len(map[row]) - 1 or val < map[row][col+1])
        if is_low_point: low_points.append([row, col])

basin_sizes = sorted([find_basin_size(map, k[0], k[1], start=True) for k in low_points], reverse=True)
print(basin_sizes)
print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])