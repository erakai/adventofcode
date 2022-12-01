lines = []
with open('day1/input.txt') as file:
    strings = file.readlines()
    for s in strings: lines.append(int(s))

# lines = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

total = 0
for i in range(len(lines)):
    if (i + 3) > len(lines) - 1: break
    if (lines[i] < lines[i+3]): total += 1

print(total)