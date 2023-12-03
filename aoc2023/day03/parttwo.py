from collections import defaultdict
import math

lines = []
debug = 0

with open("test2.txt" if debug else "input.txt") as file:
    lines = [line.strip() for line in file.readlines()]


gears = defaultdict(list)
def check_gear(i, j, num):
    if lines[i][j] == "*":
        gears[(i, j)].append(num)

for l, line in enumerate(lines):
    i = 0
    while i < len(line):
        if line[i].isnumeric():
            end = i
            while end < len(line) and line[end].isnumeric():
                end += 1

            num = int(line[i:end])
            if i > 0: check_gear(l, i - 1, num)
            if i > 0 and l > 0: check_gear(l - 1, i - 1, num)
            if i > 0 and l < len(lines) - 1: check_gear(l + 1, i - 1, num)
            if end < len(line): check_gear(l, end, num)
            if end < len(line) and l > 0: check_gear(l - 1, end, num)
            if end < len(line) and l < len(lines) - 1: check_gear(l + 1, end, num)

            for j in range(i, end):
                if l > 0: check_gear(l - 1, j, num)
                if l < len(lines) - 1: check_gear(l + 1, j, num)

            i = end
        else:
            i += 1

gears = [math.prod(p) for p in gears.values() if len(p) == 2]
ans = sum(gears)
print(ans)
