import re

with open("input.txt").read().strip() as data:
    p1 = 0
    p2 = 0
    for game, line in enumerate(data.split("\n"), start=1):
        valid = True
        min_red, min_green, min_blue = 0, 0, 0

        for s in line.split(":")[-1].split(";"):
            red = sum(int(n) for n in re.findall(r"(\d+)\sred", s))
            green = sum(int(n) for n in re.findall(r"(\d+)\sgreen", s))
            blue = sum(int(n) for n in re.findall(r"(\d+)\sblue", s))

            min_red = max(min_red, red)
            min_green = max(min_green, green)
            min_blue = max(min_blue, blue)

            if red > 12 or green > 13 or blue > 14:
                valid = False
        if valid:
            p1 += game
        p2 += min_red * min_green * min_blue

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")