lines = []
with open('day2/input.txt') as file:
    lines = file.readlines();

horiz = 0
depth = 0
for line in lines:
    m = line.split(" ")
    if m[0] == "forward":
        horiz += int(m[1])
    if m[0] == "down":
        depth += int(m[1])
    if m[0] == "up":
        depth -= int(m[1])

print(horiz * depth)