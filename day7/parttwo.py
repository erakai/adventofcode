pos = []
with open('day7/input.txt') as file:
    pos = [int(x) for x in file.readlines()[0].split(",")]

def cost(length):
    cost = 0
    for i in range(length):
        cost += (i + 1) 
    return cost

total_dist = [0] * max(pos) 
for i in range(max(pos)):
    for align in pos:
        total_dist[i] += cost((abs(i - align))) 

print(min(total_dist))
