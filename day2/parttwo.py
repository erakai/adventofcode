lines = []
with open('day2/input.txt') as file:
    lines = file.readlines()

horiz = 0
depth = 0
aim = 0
for line in lines:
    m = line.split(" ")
    if m[0] == "down":
        aim += int(m[1])
    if m[0] == "up":
        aim -= int(m[1])
    if m[0] == "forward":
        horiz += int(m[1])
        depth += (int(m[1]) * aim)

print (horiz * depth)