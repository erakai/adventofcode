lines = []
debug = 1

with open('test.txt' if debug else 'input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

cards = {}
ans = 0
for line in lines:
    tokens = line.split(":")[0].split(" ")
    num = int(tokens[len(tokens) - 1])
    line = line.strip().split(": ")[1]
    parts = line.split(" | ")
    winning = [int(x) for x in parts[0].split(" ") if len(x) > 0]
    ours = [int(x) for x in parts[1].split(" ") if len(x) > 0]
    cards[num] = (winning, ours)

cards_am = {i: 1 for i in cards}

i = 1
while i < len(lines) + 1:
    winning, ours = cards[i]

    matching = 0
    for n in ours:
        if n in winning:
            matching += 1 
    
    for j in range(1, matching + 1):
        cards_am[i + j] += cards_am[i]
    
    i += 1

print(sum(cards_am.values()))