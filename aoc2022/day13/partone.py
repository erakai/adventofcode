lines = []
debug = 0

with open('test.txt' if debug else 'input.txt') as file:
    lines = [x.strip() for x in file.readlines()]

def compare(left, right):
    if isinstance(left, list) and isinstance(right, list):
        for i in range(max(len(left), len(right))):
            if i >= len(left) and i < len(right): return True
            if i >= len(right) and i < len(left): return False
            result = compare(left[i], right[i])
            if result != None: return result
    elif isinstance(left, list) or isinstance(right, list):
        if isinstance(left, list): return compare(left, [right])
        if isinstance(right, list): return compare([left], right)
    else:
        if left < right: return True
        if left > right: return False
    return None

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

current = 1
sum = 0

l = 0
while l < len(lines):
    left = convert(lines[l])
    l += 1
    right = convert(lines[l])
    if compare(left, right): sum += current
    l += 2
    current += 1

print(sum)
