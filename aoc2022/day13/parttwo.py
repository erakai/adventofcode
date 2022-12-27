from functools import cmp_to_key

lines = []
debug = 0

with open('test.txt' if debug else 'input.txt') as file:
    lines = [x.strip() for x in file.readlines()]
    lines = list(filter(None, lines))

def compare(left, right):
    if isinstance(left, list) and isinstance(right, list):
        for i in range(max(len(left), len(right))):
            if i >= len(left) and i < len(right): return 1
            if i >= len(right) and i < len(left): return -1
            result = compare(left[i], right[i])
            if result != 0: return result
    elif isinstance(left, list) or isinstance(right, list):
        if isinstance(left, list): return compare(left, [right])
        if isinstance(right, list): return compare([left], right)
    else:
        if left < right: return 1
        if left > right: return -1
    return 0

def convert(line):
    line = line[1:-1]
    new = []
    stored = -1
    inner = 0
    for i in range(len(line)):
        if stored != -1:
            if line[i] == '[':
                inner += 1
            if line[i] == ']':
                if inner > 0:
                    inner -= 1
                else:
                    new.append(convert(line[stored:i+1]))
                    stored = -1
        elif line[i] == '[':
            stored = i
        elif line[i].isdigit():
            if i < len(line) - 1 and line[i+1].isdigit():
                new.append(int(line[i:i+2]))
                i += 1
            else:
                new.append(int(line[i]))
    return new


packets = [[[2]], [[6]]]
for line in lines: packets.append(convert(line))
finished = sorted(packets, key=cmp_to_key(compare), reverse=True)
print((finished.index([[2]]) + 1) * (finished.index([[6]]) + 1))