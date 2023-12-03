lines = []
debug = 1

with open("test.txt" if debug else "input.txt") as file:
    lines = file.readlines()

ans = 0
for line in lines:
    id = int(line.split(":")[0][4:])
    red = 0
    green = 0
    blue = 0
    for game in line.split(":")[1].split(";"):
        colors = game.split(",")
        for c in colors:
            c = c.strip()
            am = int(c.split(" ")[0])
            rgb = c.split(" ")[1].strip()
            if rgb == "red":
                red = max(am, red)
            if rgb == "blue":
                green = max(am, green)
            if rgb == "green":
                blue = max(am, blue)
    ans += red * green * blue
print(ans)
