lines = []
debug = 0

with open('test.txt' if debug else 'input.txt') as file:
    lines = file.readlines()

count = 0
for line in lines:
    tokens = line.split(',')
    pair1 = tokens[0].split('-')
    pair2 = tokens[1].split('-')
    for i in range(int(pair1[0]), int(pair1[1]) + 1):
        if i in range(int(pair2[0]), int(pair2[1]) + 1):
            count += 1
            break
    else:
        for i in range(int(pair2[0]), int(pair2[1]) + 1):
            if i in range(int(pair1[0]), int(pair1[1]) + 1):
                count += 1
                break
print(count)