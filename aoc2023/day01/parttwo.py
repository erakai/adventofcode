lines = []
debug = 0

with open("test.txt" if debug else "input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

sum = 0
newlines = []
for line in lines:
    dig = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for d in dig:
        line = line.replace(d, d[0] + str(dig.index(d) + 1) + d[-1])

    dig = ""
    for a in line:
        if a.isnumeric():
            dig += a
            break
    for a in line[::-1]:
        if a.isnumeric():
            dig += a
            break
    sum += int(dig)
print(sum)
