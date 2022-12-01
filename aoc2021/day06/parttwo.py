zeros, ones, twos, threes, fours, fives, sixes, sevens, eights = 0, 0, 0, 0, 0, 0, 0, 0, 0
fish = []
with open('day6/input.txt') as file:
    fish = [int(f) for f in (file.readlines()[0].split(","))]
for f in fish:
    if f == 0:
        zeros += 1
    if f == 1:
        ones += 1
    if f == 2:
        twos += 1
    if f == 3:
        threes += 1
    if f == 4:
        fours += 1
    if f == 5:
        fives += 1
    if f == 6:
        sixes += 1
    if f == 7:
        sevens += 1
    if f == 8:
        eights += 1 

for i in range(256):
    old_zeroes = zeros
    zeros = ones
    ones = twos
    twos = threes
    threes = fours
    fours = fives
    fives = sixes
    sixes = sevens
    sevens = eights
    eights = old_zeroes
    sixes += old_zeroes

print(zeros + ones + twos + threes + fours + fives + sixes + sevens + eights)