lines = []
with open('day3/input.txt') as file:
    lines = file.readlines()

def genoxy(pos, lines):
    zero, one = 0, 0
    for line in lines:
        if list(line)[pos] == '1': 
            one += 1
        else:
            zero += 1

    val = '1' if one >= zero else '0' 
    lines = [line for line in lines if not list(line)[pos] == val]
    if (len(lines) == 1): return lines[0]
    return genoxy(pos + 1, lines)

def co2(pos, lines):
    zero, one = 0, 0
    for line in lines:
        if list(line)[pos] == '1': 
            one += 1
        else:
            zero += 1

    val = '0' if one >= zero else '1' 
    lines = [line for line in lines if not list(line)[pos] == val]
    if (len(lines) == 1): return lines[0]
    return co2(pos + 1, lines)

print(int(genoxy(0, lines), 2) * int(co2(0, lines), 2))