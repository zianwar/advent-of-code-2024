import re

with open("input.txt", "r") as fp:
    text = "".join(fp.readlines())

pattern = r"mul\((-?\d+),(-?\d+)\)"
match = re.findall(pattern, text)

total = sum([int(x) * int(y) for x, y in match])
print(total)
