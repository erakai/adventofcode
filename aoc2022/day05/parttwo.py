lines = []
debug = 0

with open('test.txt' if debug else 'input.txt') as file:
    lines = file.readlines()

stacks = []
back = []
for i, line in enumerate(lines):
    if len(line.strip()) == 0:
        lines = lines[i:]
        break
    back.append(line)
back.reverse()
for i in range(int(back[0].split(" ")[-2].strip())):
    stacks.append([])
back.pop(0)

for i in range(len(back)):
    back[i] = back[i].replace("[", "")
    back[i] = back[i].replace("]", "").strip()
    back[i] = back[i].replace("    ", " ")
    for i, val in enumerate(back[i].split(" ")):
        if len(val) != 0:
            stacks[i].append(val)

for line in lines:
    if len(line.strip()) == 0:
        continue
    
    amount = int(line[line.index('move') + 4: line.index('from')])
    src = int(line[line.index('from') + 4: line.index('to')])
    dest = int(line[line.index('to') + 2:])

    for i in range(amount):
        val = stacks[src - 1].pop(len(stacks[src-1]) - (amount - i))
        stacks[dest - 1].append(val)

for i in stacks:
    print(i[-1], end="")
print()