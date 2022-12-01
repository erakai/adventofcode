lines = []

with open('input.txt') as file:
    lines = file.readlines()

max = 0
current = 0

for line in lines:
    if len(line.strip()) == 0:
        if current > max:
            max = current
        current = 0
    else:
        current = current + int(line)

print(max)
