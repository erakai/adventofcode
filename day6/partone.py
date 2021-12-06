class Fish:
    def __init__(self, days):
        self.days = days

    def age(self):
        self.days -= 1
        if (self.days < 0):
            self.days = 6
            return Fish(8)

fish = []
with open('day6/input.txt') as file:
    fish = [Fish(int(x)) for x in file.readlines()[0].split(",")]

for i in range(256):
    too_add = []
    for f in fish:
        spawn = f.age()
        if not spawn == None:
            too_add.append(spawn)
    fish.extend(too_add)

print(len(fish))