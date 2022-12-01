lines = open('day14/input.txt').read().splitlines()

template = lines[0]
rules_arr = [lines[i].upper().split(' -> ') for i in range(2, len(lines))]

rules = {}
count = {}
initial_pairs = {}

def add_pair(pair, num=1):
    if pair not in initial_pairs.keys(): initial_pairs[pair] = 0
    initial_pairs[pair] += num

for r in rules_arr:
    rules[r[0]] = r[1]

for i in range(len(template) - 1):
    add_pair(template[i:i+2])

for i in range(len(template)):
    if template[i] not in count.keys(): count[template[i]] = 0
    count[template[i]] += 1

for i in range(40):
    pair_copy = initial_pairs.copy()
    for p in pair_copy.keys():
        if p in rules.keys():
            if rules[p] not in count.keys(): count[rules[p]] = 0
            count[rules[p]] += pair_copy[p]
            initial_pairs[p] -= pair_copy[p] 
            add_pair((p[0] + rules[p]), num=pair_copy[p])
            add_pair((rules[p] + p[1]), num=pair_copy[p])

print('Sum:', sum(count.values()))
print('Max:', max(count.values()))
print('Min:', min(count.values()))
print('Diff:', max(count.values()) - min(count.values()))