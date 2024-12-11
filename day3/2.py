import re

with open("input.txt", "r") as fp:
    text = "".join(fp.readlines())

pattern = r"mul\((-?\d+),(-?\d+)\)|(do\(\)|don't\(\))"
match = re.findall(pattern, text)

total = 0
enabled = True
for x, y, ins in match:
    if ins:
        if ins == "do()":
            enabled = True
        elif ins == "don't()":
            enabled = False
        continue

    if enabled:
        total += int(x) * int(y)

print(total)
