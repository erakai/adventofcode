lines = []
debug = 0

with open('test.txt' if debug else 'input.txt') as file:
    lines = file.readlines()

total = 0

win = {
    'A': 2,
    'B': 3,
    'C': 1,
}

draw = {
    'A': 1,
    'B': 2,
    'C': 3
}

lose = {
    'A': 3,
    'B': 1,
    'C': 2
}

scores = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}


total = 0
for line in lines:
    tokens = line.split()
    current = 0

    if tokens[1] == 'X':
        current += lose[tokens[0]]
    elif tokens[1] == 'Y':
        current += draw[tokens[0]]
        current += 3
    elif tokens[1] == 'Z':
        current += 6
        current += win[tokens[0]]

    total += current

print(total)
