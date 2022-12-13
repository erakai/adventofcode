lines = []
debug = 0

with open('test.txt' if debug else 'input.txt') as file:
    lines = file.readlines()
lines.append('\n')

def create(og):
    return [(og % i) for i in range(2, 24)]

def update(og):
    return [(og[i-2] % i) for i in range(2, 24)]

class Monkey:
    def __init__(self, items, op, tests):
        self.items = items
        self.op = op
        self.tests = tests # [div by, true, false]
        self.act = 0
    
    def test(self, item):
        return self.tests[1:][item[self.tests[0]-2] != 0]

    def add(self, item):
        self.items.append(item)

    def operate(self, item):
        operation = self.op.split("new = old ")[1][0].strip()
        operand = self.op.split(operation + ' ')[1].strip()

        if operand == 'old': 
            operand = item
            for i in range(len(item)):
                if operation == '*':
                    item[i] *= operand[i]
                elif operation == '+':
                    item[i] += operand[i]
                elif operation == '-':
                    item[i] -= operand[i]
        else:
            operand = int(operand)
            for i in range(len(item)):
                if operation == '*':
                    item[i] *= operand
                elif operation == '+':
                    item[i] += operand
                elif operation == '-':
                    item[i] -= operand
        item = update(item)
        
        return item
    
    def run(self, monkeys):
        for item in self.items:
            self.act += 1
            new = self.operate(item)
            monkeys[self.test(new)].add(new)
        self.items = []
        
monkeys = []
items = []
operation = ''
test = []

for line in lines:
    line = line.strip()

    if len(line) == 0:
        monkeys.append(Monkey(items, operation, test))
        items = []
        operations = ''
        test = []
    
    if line.startswith('Monkey'):
        continue

    if line.startswith('Starting items:'):
        line = line.split('Starting items:')[1]
        nums = line.split(", ")
        for num in nums:
            num = num.strip()
            if len(num) != 0:
                items.append(create(int(num)))

    if line.startswith('Operation:'):
        operation = line

    if line.startswith('Test'):
        test.append(int(line.split(" divisible by")[1].strip()))

    if line.startswith('If true:'):
        test.append(int(line.split("throw to monkey ")[1].strip()))

    if line.startswith('If false:'):
        test.append(int(line.split("throw to monkey")[1].strip()))

for i in range(10000):
    for m, monkey in enumerate(monkeys):
        monkey.run(monkeys)

activities = [m.act for m in monkeys]
activities.sort(reverse=True)
print(activities)
print(activities[0] * activities[1])