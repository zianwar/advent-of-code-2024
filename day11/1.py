from __future__ import annotations

import os

os.system("clear")

with open("input.txt") as fp:
    data = fp.read()


# [125, 17] → [253000, 1, 7]
def blink(stones: list[int]) -> list[int]:
    result: list[int] = []
    for stone in stones:
        if stone == 0:
            result.append(1)
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            mid = len(str(stone)) // 2
            left = s[:mid]
            right = s[mid:]
            result += [int(left), int(right)]
        else:
            result.append(stone * 2024)
    return result


stones = [int(s) for s in data.split()]
for i in range(25):
    stones = blink(stones)

print(len(stones))
