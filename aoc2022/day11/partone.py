lines = []
debug = 0

with open('test.txt' if debug else 'input.txt') as file:
    lines = file.readlines()
lines.append('\n')

class Monkey:
    def __init__(self, items, op, tests):
        self.items = items
        self.op = op
        self.tests = tests # [div by, true, false]
        self.act = 0
    
    def test(self, item):
        return self.tests[1:][item % int(self.tests[0]) != 0]

    def add(self, item):
        self.items.append(item)

    def operate(self, item):
        operation = self.op.split("new = old ")[1][0].strip()
        operand = self.op.split(operation + ' ')[1].strip()
        if operand == 'old': operand = item
        operand = int(operand)
        
        if operation == '*':
            item *= operand
        elif operation == '+':
            item += operand
        elif operation == '-':
            item -= operand
        
        return item
    
    def run(self, monkeys):
        for item in self.items:
            self.act += 1
            new = int(self.operate(item) / 3)
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
        line = line[16:]
        nums = line.split(", ")
        for num in nums:
            num = num.strip()
            if len(num) != 0:
                items.append(int(num))

    if line.startswith('Operation:'):
        operation = line

    if line.startswith('Test'):
        test.append(int(line.split(" divisible by")[1].strip()))

    if line.startswith('If true:'):
        test.append(int(line.split("throw to monkey ")[1].strip()))

    if line.startswith('If false:'):
        test.append(int(line.split("throw to monkey")[1].strip()))

for i in range(20):
    for m, monkey in enumerate(monkeys):
        monkey.run(monkeys)

activities = [m.act for m in monkeys]
activities.sort(reverse=True)
print(activities)
print(activities[0] * activities[1])