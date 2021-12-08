lines = []
with open('day8/input.txt') as file:
    lines = file.readlines()

count = 0

for line in lines:
    key = line.strip().split(" |")[0]
    code = line.strip().split("| ")[1]

    uniq_seg = []
    for segment in key.split(" "):
        if len(segment) in [2, 3, 4, 7]:
            uniq_seg.append(segment)
    for c in code.split(" "):
        """for seg in uniq_seg:
            eq = True
            for char in list(c.strip()):
                if char not in list(seg):
                   eq = False 
                   break
            if eq: 
                count += 1
                break"""
        if len(c) in [2, 3, 4, 7]: count += 1
            
print(count)