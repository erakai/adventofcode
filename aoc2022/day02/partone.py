lines = []
debug = 0

with open('test.txt' if debug else 'input.txt') as file:
    lines = file.readlines()

total = 0

key = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
}

scores = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

across ={
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

total = 0
for line in lines:
    tokens = line.split()
    current = 0

    if key[tokens[0]] == tokens[1]:
        current += 6
    elif across[tokens[0]] == tokens[1]:
        current += 3

    current += scores[tokens[1]]
    total += current

print(total)
