lines = []
debug = 0

with open('test.txt' if debug else 'input.txt') as file:
    lines = file.readlines()

cards = {}
ans = 0
for line in lines:
    line = line.strip().split(": ")[1]
    parts = line.split(" | ")
    winning = [int(x) for x in parts[0].split(" ") if len(x) > 0]
    ours = [int(x) for x in parts[1].split(" ") if len(x) > 0]

    matching = 0
    for i in ours:
        if i in winning:
            matching += 1 
print(ans)