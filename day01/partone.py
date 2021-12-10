lines = []
with open('day1/input.txt') as file:
    lines = file.readlines()

total_lines_greater = 0
previous = None
for line in lines: 
    if previous == None:
        previous = int(line)
    else:
        if int(line) > previous:
            total_lines_greater += 1
        previous = int(line)

print(total_lines_greater)
