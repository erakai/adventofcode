lines = []
debug = 0

with open('test.txt' if debug else 'input.txt') as file:
    lines = file.readlines()

current = []
common = []
for line in lines:
    if len(current) == 3:
        for i in current[0]: 
            if i in current[1] and i in current[2]:
                common.append(i)
                break
        current = [line.strip()]
    else:
        current.append(line.strip())


# inefficiency!!
if len(current) == 3:
    for i in current[0]: 
        if i in current[1] and i in current[2]:
            common.append(i)
            break

total = 0 
for i in common:
    if i.isupper():
        total += (ord(i) - 38)
    else:
        total += (ord(i)- 96)

print(total)
