lines = []
debug = 0

with open('test.txt' if debug else 'input.txt') as file:
    lines = file.readlines()

positions = [(0, 0)]
head = [0, 0]
tail = [0, 0]

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

for line in lines:
    dir = line.split(" ")[0]
    am = int(line.split(" ")[1])

    for i in range(am):
        move(dir, head)
        if not is_touching(head, tail):
            if head[0] == tail[0] or head[1] == tail[1]:
                move(dir, tail)
            else:
                if abs(head[0] - tail[0]) == 1:
                    if head[0] - tail[0] > 0:
                        tail[0] += 1
                    else:
                        tail[0] -= 1 
                else:
                    if head[1] - tail[1] > 0:
                        tail[1] += 1
                    else:
                        tail[1] -= 1 
                move(dir, tail) 
            positions.append((tail[0], tail[1]))

print(len(set(positions)))

