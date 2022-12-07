lines = []
debug = 0

with open('test.txt' if debug else 'input.txt') as file:
    lines = file.readlines()

class Folder:
    def __init__(self, name='/', parent=None, children=[], size=0):
        self.parent = parent
        self.name = name
        self.children = children
        self.size = size

    def __str__(self):
        return ('Name: ' + self.name +', Size: ' + str(self.size))

lines = lines[1:]
system = Folder()
folders = [system]
parent = None
current_folder = system

in_ls = False

for line in lines:
    if line.startswith("$"):
        if in_ls:
            in_ls = False
           
        if line.startswith("$ cd"):
            name = line.split("cd ")[1].strip()
            if name == '..':
                current_folder = parent
                parent = current_folder.parent
            else:
                parent = current_folder
                for folder in current_folder.children:
                    if folder.name == name:
                        current_folder = folder
                        break
                else:
                    current_folder = Folder(name, parent, [], 0)
                    parent.children.append(current_folder)
                    folders.append(current_folder)

        elif line.startswith("$ ls"):
            in_ls = True
    elif in_ls:
        if not line.startswith("dir"):
            size = int(line.split(" ")[0])
            current_folder.size += size
            current = current_folder
            while not current.parent == None:
                current = current.parent
                current.size += size
        else:
            new = Folder(line.split("dir ")[1].strip(), current_folder, [], 0)
            current_folder.children.append(new)
            folders.append(new)

sum = 0
for folder in folders:
    if folder.size <= 100000:
        print(folder.size, end=' ')
        sum += folder.size

print('\nTotal: ' + str(sum))
