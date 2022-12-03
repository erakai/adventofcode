lines = []
debug = 0

with open('test.txt' if debug else 'input.txt') as file:
    lines = file.readlines()

common = []
for ruck in lines:
    mid = len(ruck)/2
    comp1 = ruck[:int(mid)]
    comp2 = ruck[int(mid):]
    for i in comp1: 
        if i in comp2:
            common.append(i)
            break

total = 0 
for i in common:
    if i.isupper():
        total += (ord(i) - 38)
    else:
        total += (ord(i)- 96)

print(total)
