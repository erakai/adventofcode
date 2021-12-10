lines = []
with open('day8/input.txt') as file:
    lines = file.readlines()

count = 0

"""
This is some of the worst code I have written in my life. I misread the problem at 1 am and wrote random code because it seemed impossible
for the next 2 hours while sitting in a 40 degree room. Then I went to sleep and realized I read the problem wrong and solved it in
10 minutes in the morning.
"""

def clean_items(char_list):
    for k, v in char_list.items():
        if len(v) == 0: continue
        in_all = v[0]
        for possible_char in v:
            for c in in_all:
                if c not in possible_char:
                    in_all.remove(c)
        char_list[k] = in_all
    return char_list

for line in lines:
    key = line.strip().split(" |")[0]
    code = line.strip().split("| ")[1]

    poss = [[] for _ in range(10)] 
    seven_display = {2: [1], 3: [7], 4: [4], 5: [2, 3, 5], 6: [0, 6, 9], 7: [8]}
    uniques = [2, 3, 4]
    locked = []
    chars = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': []}
    locked_chars = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': []}
    seg = {0: ['a', 'b', 'c', 'e', 'f', 'g'], 1: ['c', 'f'], 2: ['a', 'c', 'd', 'e','g'], \
        3: ['a', 'c', 'd', 'f', 'g'], 4: ['b', 'c', 'd', 'f'], 5: ['a', 'b', 'd', 'f', 'g'], \
        6: ['a', 'b', 'd', 'e', 'f', 'g'], 7: ['a', 'c', 'f'], 8: list(chars), 9: ['a', 'b', 'c', 'd', 'f', 'g']}
    key_words = [[] for _ in range(10)]

    # Adds the key segment to each number it could represent
    for segment in key.split(" "):
        for k in seven_display[len(segment)]: poss[k].append(segment)

    for i in uniques: # For every unique number where we know what values it can be 
        for p in poss[seven_display[i][0]]: # Each possibility for each unique number
            key_words[seven_display[i][0]] = p
            for c in seg[seven_display[len(p)][0]]: # Each letter segment in the number
                locked_chars[c].append(list(p)) # Add each segment in the possibility as a possible value for each letter in the number
                locked.append(c)

    # Convert 
    for i in range(10): # Each number and the possibilities for them
        for p in poss[i]: # Each possibility for each number
            for c in seg[i]: # Each letter segment in the number
                if c not in locked: # If the letter isn't already claimed by a unique value
                    chars[c].append(list(p)) # Add each segment in the possibility as a possible value for each letter in the number

    # Go through each letter and its possible segments and eliminate everything that isn't in every segment
    # clean_items(chars) 
    clean_items(locked_chars)
    for c in chars:
        chars[c] = list(set(sum(chars[c], [])))

    # if an element only exists in one list it will be removed from the others
    for c in locked_chars:
        total_seen = 0
        for k in locked_chars:
            if c in locked_chars[k]: total_seen += 1
        if total_seen == 1:
            for m in locked_chars:
                if c in locked_chars[m]: 
                    locked_chars[m] = [c]            
                    for k in chars:
                        chars[k] = [val for val in chars[k] if val != c]
                break

    # elements will be removed from all lists except the shortest ones they are in
    for c in locked_chars:
        shortest_occurrence = 100000
        for k in locked_chars:
            if c in locked_chars[k]: shortest_occurrence = min(shortest_occurrence, len(locked_chars[k]))
        for k in locked_chars:
            if c in locked_chars[k] and not len(locked_chars[k]) == shortest_occurrence:
                locked_chars[k] = [val for val in locked_chars[k] if val != c]
        for k in chars:
            if not shortest_occurrence == 100000:
                chars[k] = [val for val in chars[k] if val != c]

    for c in chars:
        chars[c] = locked_chars[c] + chars[c]

    #print(locked_chars)
    #print(chars)

    for segment in key.split(" "):
        if len(segment) in uniques: continue
        elif len(segment) == 5:
            if set(chars['c']).issubset(list(segment)):
               key_words[3] = segment
            elif set(chars['b']).issubset(list(segment)): 
                key_words[5] = segment
            else:
                key_words[2] = segment
        elif len(segment) == 6:
            if not set(chars['c']).issubset(list(segment)) and set(chars['b']).issubset(list(segment)):
                key_words[6] = segment
            elif not set(chars['d']).issubset(list(segment)):
                key_words[0] = segment
            else:
                key_words[9] = segment
        else:
            key_words[8] = segment

    print(key_words)

    # Using chars as a key for each letter, convert each code into a number and add it to the count.
    entry = ""
    for c in code.split(" "):
        for i in range(10):
            if set(list(c)) == set(list(key_words[i])):
                entry += str(i)
                break

    count += int(entry)

print(count)