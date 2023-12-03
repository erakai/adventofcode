lines = []
debug = 0

with open("test.txt" if debug else "input.txt") as file:
    lines = [line.strip() for line in file.readlines()]


def is_symbol(c):
    return c != "." and not c.isnumeric()


ans = 0
for l, line in enumerate(lines):
    i = 0
    while i < len(line):
        c = line[i]

        if c.isnumeric():
            # find length of number
            end = i
            while end < len(line) and line[end].isnumeric():
                end += 1

            num = int(line[i:end])
            is_part = False
            if i > 0 and is_symbol(line[i - 1]):
                is_part = True
            if i > 0 and l > 0 and is_symbol(lines[l - 1][i - 1]):
                is_part = True
            if i > 0 and l < len(lines) - 1 and is_symbol(lines[l + 1][i - 1]):
                is_part = True
            if end < len(line) - 1 and is_symbol(line[end]):
                is_part = True
            if end < len(line) - 1 and l > 0 and is_symbol(lines[l - 1][end]):
                is_part = True
            if (
                end < len(line) - 1
                and l < len(lines) - 1
                and is_symbol(lines[l + 1][end])
            ):
                is_part = True

            # above
            if l > 0:
                for j in range(i, end):
                    if is_symbol(lines[l - 1][j]):
                        is_part = True

            # below
            if l < len(lines) - 1:
                for j in range(i, end):
                    if is_symbol(lines[l + 1][j]):
                        is_part = True

            if is_part:
                i = end + 1
                ans += num
                continue
        i += 1

print(ans)
