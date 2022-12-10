lines = []
debug = 0

with open('test.txt' if debug else 'input.txt') as file:
    lines = file.readlines()

stop = 20
x = 1
cycle = 0

def check(x, cycle):
    if abs(horizontal(cycle) - x) <= 1:
        print('#', end='')
    else:
        print('.', end='')
    if cycle % 40 == 0: print()

def horizontal(cycle):
    return cycle % 40

for line in lines:
    instr = line.split(" ")[0].strip()

    if instr == 'noop': 
        cycle += 1
        check(x, cycle)
        continue

    if instr == 'addx':
        am = int(line.split(" ")[1])
        cycle += 1
        check(x, cycle)
        cycle += 1
        x += am
        check(x, cycle)
