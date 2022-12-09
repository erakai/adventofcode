lines = []
debug = 0

with open('test2.txt' if debug else 'input.txt') as file:
    lines = file.readlines()

positions = set([(0, 0)])
knots = [[0, 0] for _ in range(10)]

def is_touching(one, two):
    return ((one[0] == two[0] - 1 and one[1] == two[1] - 1) or
            (one[0] == two[0] + 1 and one[1] == two[1] + 1) or
            (one[0] == two[0] - 1 and one[1] == two[1] + 1) or
            (one[0] == two[0] + 1 and one[1] == two[1] - 1) or
            (one[0] == two[0] - 1 and one[1] == two[1]) or 
            (one[0] == two[0] + 1 and one[1] == two[1]) or 
            (one[1] == two[1] - 1 and one[0] == two[0]) or
            (one[1] == two[1] + 1 and one[0] == two[0]) or 
            (one[0] == two[0] and one[1] == two[1]))

def move(dir, arr):
    if dir == 'R': arr[0] += 1
    if dir == 'L': arr[0] -= 1
    if dir == 'U': arr[1] += 1
    if dir == 'D': arr[1] -= 1

def new_move(one, two):
    if one[0] == two[0]:
        if one[1] > two[1]:
            two[1] += 1
        else:
            two[1] -= 1
        return True
    elif one[1] == two[1]:
        if one[0] > two[0]:
            two[0] += 1
        else:
            two[0] -= 1
        return True
    return False

def run_edge_case(one, two):
    if (one[0] == two[0] - 2 and one[1] == two[1] - 2):
        two[0] -= 1
        two[1] -= 1
    elif (one[0] == two[0] + 2 and one[1] == two[1] + 2): 
        two[0] += 1
        two[1] += 1
    elif (one[0] == two[0] - 2 and one[1] == two[1] + 2): 
        two[0] -= 1
        two[1] += 1
    elif (one[0] == two[0] + 2 and one[1] == two[1] - 2):
        two[0] += 1
        two[1] -= 1

for line in lines:
    dir = line.split(" ")[0]
    am = int(line.split(" ")[1])

    for i in range(am):
        move(dir, knots[0])
        for i in range(1, 10):
            if not is_touching(knots[i-1], knots[i]):
                if not new_move(knots[i-1], knots[i]): 
                    if abs(knots[i-1][0] - knots[i][0]) == 1:
                        if knots[i-1][0] - knots[i][0] > 0:
                            knots[i][0] += 1
                        else:
                            knots[i][0] -= 1 
                    if abs(knots[i-1][1] - knots[i][1]) == 1:
                        if knots[i-1][1] - knots[i][1] > 0:
                            knots[i][1] += 1
                        else:
                            knots[i][1] -= 1
                    new_move(knots[i-1], knots[i]) 
                    run_edge_case(knots[i-1], knots[i])

                if i == 9:
                    positions.add((knots[9][0], knots[9][1]))

print(len(positions))

