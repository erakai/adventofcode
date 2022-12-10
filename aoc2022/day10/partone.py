lines = []
debug = 1

with open('test.txt' if debug else 'input.txt') as file:
    lines = file.readlines()

stop = 20
total = [0]
x = 1
cycle = 0

def check(total, cycle):
    if cycle == stop or (cycle - 20) % 40 == 0: 
        total[0] += (cycle * x)

for line in lines:
    instr = line.split(" ")[0].strip()

    if instr == 'noop': 
        cycle += 1
        check(total, cycle)
        continue

    if instr == 'addx':
        am = int(line.split(" ")[1])
        cycle += 1
        check(total, cycle)
        cycle += 1
        check(total, cycle)
        x += am


print(x)
print(total[0])