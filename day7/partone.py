pos = []
with open('day7/input.txt') as file:
    pos = [int(x) for x in file.readlines()[0].split(",")]

total_dist = [0] * len(pos) 
for i in range(len(pos)):
    for align in pos:
        total_dist[i] += abs(align - pos[i])

print(min(total_dist))
