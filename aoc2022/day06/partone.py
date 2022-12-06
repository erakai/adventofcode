import string

lines = []
debug = 0

with open('test.txt' if debug else 'input.txt') as file:
    lines = file.readlines()

input = list(lines[0])

for i, val in enumerate(input):
    if i < 4: continue

    count = dict.fromkeys(string.ascii_lowercase, 0)
    for char in input[i-4:i]:
        count[char] += 1

    if max(count.values()) <= 1:
        print(i)
        break
    
