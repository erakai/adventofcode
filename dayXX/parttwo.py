lines = []
debug = 0

with open('test.txt' if debug else 'input.txt') as file:
    lines = [line.strip() for line in file.readlines()]
