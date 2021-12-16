lines = open('day14/input.txt').read().splitlines()

template = lines[0]
rules = [lines[i].upper().split(' -> ') for i in range(2, len(lines))]

for i in range(10):
    copy = template
    counter = 1
    for i in range(len(template)):
        for r in rules:
            if (template[i:i+2] == r[0]):
                copy = copy[:i + counter] + r[1] + copy[i + counter:]
                counter += 1
    template = copy

template = list(template)
most_common = max(set(template), key=template.count)
least_common = min(set(template), key=template.count)
print(template.count(most_common) - template.count(least_common))