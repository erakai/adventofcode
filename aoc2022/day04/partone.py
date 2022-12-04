lines = []
debug = 0

with open('test.txt' if debug else 'input.txt') as file:
    lines = file.readlines()

count = 0
for line in lines:
    tokens = line.split(',')
    pair1 = tokens[0].split('-')
    pair2 = tokens[1].split('-')
    if (int(pair1[0]) >= int(pair2[0]) and int(pair1[1]) <= int(pair2[1])):
        count += 1 
    elif (int(pair2[0]) >= int(pair1[0]) and int(pair2[1]) <= int(pair1[1])):
        count += 1

print(count)