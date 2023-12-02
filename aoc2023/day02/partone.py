lines = []
debug = 0

with open("test.txt" if debug else "input.txt") as file:
    lines = file.readlines()

red = 12
green = 13
blue = 14

ans = 0
for line in lines:
    id = int(line.split(":")[0][4:])
    count = True
    for game in line.split(":")[1].split(";"):
        colors = game.split(",")
        for c in colors:
            c = c.strip()
            am = int(c.split(" ")[0])
            rgb = c.split(" ")[1].strip()
            if rgb == "red" and am > red:
                count = False
            if rgb == "blue" and am > blue:
                count = False
            if rgb == "green" and am > green:
                count = False
    if count:
        ans += id
print(ans)
