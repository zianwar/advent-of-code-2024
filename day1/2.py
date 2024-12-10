from collections import Counter

with open("input.txt", "r") as fp:
    lines = fp.readlines()

multiplicands = []
multipliers = Counter()
for line in lines:
    left, right = line.split("   ")
    multiplicands.append(int(left))
    multipliers.update([int(right)])

total = sum([x * multipliers[x] for x in multiplicands])
print(total)
