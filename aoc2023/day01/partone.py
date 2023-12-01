lines = []
debug = 0

with open("test.txt" if debug else "input.txt") as file:
    lines = file.readlines()

sum = 0
newlines = []
for line in lines:
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
