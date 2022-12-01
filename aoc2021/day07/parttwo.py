pos = []
with open('day7/test.txt') as file:
    pos = [int(x) for x in file.readlines()[0].split(",")]

def cost(length):
    return sum(range(1, length+1))

total_dist = [0] * max(pos) 
for i in range(max(pos)):
    for align in pos:
        total_dist[i] += cost((abs(i - align))) 

print(min(total_dist))
