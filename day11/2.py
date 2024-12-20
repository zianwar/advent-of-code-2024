from __future__ import annotations

import os
from functools import cache

os.system("clear")

with open("input.txt") as fp:
    data = fp.read()


# blink(17, 0) -> 1
@cache
def blink(stone: int, count: int) -> int:
    if count == 0:
        return 1
    elif stone == 0:
        return blink(1, count - 1)
    elif (l := len(s := str(stone))) % 2 == 0:
        mid = l // 2
        return blink(int(s[:mid]), count - 1) + blink(int(s[mid:]), count - 1)
    else:
        return blink(stone * 2024, count - 1)


stones = [int(s) for s in data.split()]

total = 0
for stone in stones:
    total += blink(stone, 75)

print(total)
