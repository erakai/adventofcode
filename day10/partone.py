lines = []
with open('day10/input.txt') as file:
    lines = file.readlines()

values = {')': 1, ']': 2, '}': 3, '>': 4}
db = {'(': ')', '[': ']', '{': '}', '<': '>'}
scores = []
completion_strings = []

for line in lines:
    tokens = list(line.strip()) 
    queue = []
    for t in tokens:
        if t in db.keys():
            queue.append(t)
        else:
            if not t == db[queue.pop(len(queue) - 1)]:
                break
    else:
        queue.reverse()
        score = 0 
        for c in queue:
            score *= 5
            score += values[db[c]]  
        scores.append(score)

print(sorted(scores)[int(len(scores) / 2)])