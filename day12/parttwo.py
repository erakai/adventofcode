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
        if not self.name == 'start': self.traveled = False

    def print(self):
        print('Name: ', self.name, 'Traveled:', self.traveled, '|| Connections: [', end="")
        for c in self.connections: print(c.name + ', ', end= "")
        print(']')
        
caves = []
start, end = Cave('start', False), Cave('end', True)
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

""" Recursive function doesn't work
def travel(start, end, has_twice):
    if start == end: return 1 
    paths, cons, o_length = 0, list(start.connections), len(start.connections)
    if has_twice: 
        for c in start.connections: 
            if not c.big and not c.traveled: cons.append(c)

    for i in range(len(cons)):
        if not cons[i].traveled:
            will_have_twice = has_twice if (i < o_length) else False
            used_twice = has_twice and not will_have_twice

            if not used_twice: cons[i].travel() 
            paths += travel(cons[i], end, will_have_twice) 
            cons[i].reset()
    return paths
"""

paths_count = 0
paths_batch = []
frontier = []
frontier.append([start, "start-", [start], True])
while len(frontier) != 0:
    frontier_copy = list(frontier)
    frontier.clear()
    for nodes in frontier_copy:
        current = nodes[0]
        for con in current.connections:
            p = nodes[1]
            visited_nodes = list(nodes[2])
            if con not in visited_nodes:
                p += (con.name + "-")
                if not con.big: visited_nodes.append(con)
                if con.name == 'end':
                    if p[0:len(p)-1] not in paths_batch:
                        paths_batch.append(p[0:len(p)-1])
                else: 
                    frontier.append([con, p, list(visited_nodes), nodes[3]])
                    if nodes[3] and not con.big:
                        visited_nodes.remove(con)
                        frontier.append([con, p, visited_nodes, False])
    paths_count += len(paths_batch)
    paths_batch.clear()

print(paths_count)