lines = []
with open('day9/input.txt') as file:
    lines = file.readlines()

map = [list(l.strip()) for l in lines]
map = [[int(c) for c in r] for r in map]

risk_sum = 0
for row in range(len(map)):
    for col in range(len(map[row])):
        val = map[row][col]
        is_low_point =  (row == 0 or val < map[row-1][col]) and \
                        (row == len(map) - 1 or val < map[row+1][col] ) and \
                        (col == 0 or val < map[row][col-1]) and \
                        (col == len(map[row]) - 1 or val < map[row][col+1])
        if is_low_point: risk_sum += (val + 1)

print(risk_sum)