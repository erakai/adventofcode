lines = []
with open('day3/input.txt') as file:
    lines = file.readlines()

one_rate = {}
zero_rate = {}
for i in range(len(lines[0]) - 1):
    one_rate[i] = 0
    zero_rate[i] = 0 

for line in lines:
    bits = list(line)
    for i in range(len(bits) - 1):
        if (bits[i] == '1'):
            one_rate[i] += 1
        else:
            zero_rate[i] += 1

gamma = ""
epsilon = ""
for bit in one_rate:
    val = one_rate[bit]
    gamma += ('1' if val > zero_rate[bit] else '0')
    epsilon += ('0' if val > zero_rate[bit] else '1')

print(gamma + " || " + epsilon)
print(int(gamma, 2) * int(epsilon, 2))
    