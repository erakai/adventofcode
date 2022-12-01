lines = []
with open('day12/input.txt') as file:
    lines = file.readlines()

class Cave:
    def __init__(self, name, big):
        self.name = name
        self.big = big
        self.connections = [] 
        self.traveled = False

    def make_connection(self, cave):
        self.connections.append(cave)
    
    def travel(self):
        if not self.big: self.traveled = True

    def reset(self):
        self.traveled = False

    def print(self):
        print('Name: ', self.name, '|| Connections: [', end="")
        for c in self.connections: print(c.name + ', ', end= "")
        print(']')
        
caves = []
start, end = Cave('start', False), Cave('end', False)
caves.append(start)
caves.append(end)
for line in lines:
    first_cave = line.split("-")[0].strip()
    second_cave = line.split("-")[1].strip()
    fo, so = None, None

    for c in caves:
        if first_cave == c.name: fo = c
        if second_cave == c.name: so = c

    if so == None:
        so = Cave(second_cave, second_cave.isupper())
        caves.append(so)
    if fo == None:
        fo = Cave(first_cave, first_cave.isupper())
        caves.append(fo)
    fo.make_connection(so)
    so.make_connection(fo)


def travel(start, end, grid):
    if start == end: return 1
    paths = 0
    for c in start.connections:
        if not c.traveled:
            c.travel()
            paths += travel(c, end, grid)
            c.reset()
    return paths


start.traveled = True
print(travel(start, end, caves))
    
