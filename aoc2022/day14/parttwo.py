lines = []
debug = 0

with open('test.txt' if debug else 'input.txt') as file:
    lines = [x.strip() for x in file.readlines()]

blocked = set()
bottom = -1

def block(elem):
    global bottom

    if elem[1] > bottom:
        bottom = elem[1]
    blocked.add(elem)

def bar(one, two):
    diff = 0
    if one[0] == two[0]:
        if one[1] > two[1]:
            while (two[1] + diff <= one[1]):
                block((one[0], two[1] + diff))
                diff += 1
        else:
            while (one[1] + diff <= two[1]):
                block((one[0], one[1] + diff))
                diff += 1
    else:
        if one[0] > two[0]:
            while (two[0] + diff <= one[0]):
                block((two[0] + diff, one[1]))
                diff += 1
        else:
            while (one[0] + diff <= two[0]):
                block((one[0] + diff, two[1]))
                diff += 1

for line in lines:
    tokens = [int(x) for x in line.replace(' -> ', ',').split(",")]
    i = 0
    while i < len(tokens) - 2:
        bar((tokens[i], tokens[i+1]), (tokens[i+2], tokens[i+3]))
        i += 2

bottom += 2
count = 0
while True:
    sand = (500, 0)
    count += 1
    while True:
        if sand[1] == bottom - 1:
            block(sand)
            break
        elif (sand[0], sand[1]+1) not in blocked:
            sand = (sand[0], sand[1]+1)
        elif (sand[0]-1, sand[1]+1) not in blocked:
            sand = (sand[0]-1, sand[1]+1)
        elif (sand[0]+1, sand[1]+1)not in blocked:
            sand = (sand[0]+1, sand[1]+1)
        else:
            if sand == (500, 0):
                print(count)
                exit()
            block(sand)
            break