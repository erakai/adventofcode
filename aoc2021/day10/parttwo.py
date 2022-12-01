# I changed like 5 lines between my p1 and p2 and didn't bother making a new file.

lines = []
with open('day10/input.txt') as file:
    lines = file.readlines()

values = {')': 1, ']': 2, '}': 3, '>': 4}
db = {'(': ')', '[': ']', '{': '}', '<': '>'}
scores = []
completion_strings = []

for line in lines:
    tokens = list(line.strip()) 
    stack = []
    for t in tokens:
        if t in db.keys():
            stack.append(t)
        else:
            if not t == db[stack.pop(len(stack) - 1)]:
                break
    else:
        stack.reverse()
        score = 0 
        for c in stack:
            score *= 5
            score += values[db[c]]  
        scores.append(score)

print(sorted(scores)[int(len(scores) / 2)])