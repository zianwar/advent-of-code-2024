import os
from dataclasses import dataclass
from pprint import pprint
from typing import Self

os.system("clear")


@dataclass
class File:
    id: int
    start: int
    size: int


@dataclass
class FragmentationTree:
    blocks: list[int | None]
    index: int
    depth: int
    capacity: int = -1
    left: Self | None = None
    right: Self | None = None

    def __post_init__(self):
        print(f"{self.depth * " "}{self.blocks}")
        self.capacity = len([b for b in self.blocks if b is None])
        if self.capacity in (0, len(self.blocks)):
            return

        mid = len(self.blocks) // 2
        left, right, curr = mid, mid, self.blocks[mid]
        while True:
            if left >= 0 and self.blocks[left] != curr:
                mid = left + 1
                break
            elif right < len(self.blocks) and self.blocks[right] != curr:
                mid = right
                break
            else:
                left -= 1
                right += 1

        self.left = FragmentationTree(self.blocks[:mid], 0, self.depth + 1)
        self.right = FragmentationTree(self.blocks[mid:], mid, self.depth + 1)


@dataclass
class Disk:
    blocks: list[int | None]

    @staticmethod
    def parse(data: str) -> "Disk":
        blocks: list[int | None] = []
        for i, size in enumerate(data):
            blocks += [i // 2 if i % 2 == 0 else None] * int(size)
        return Disk(blocks)

    def files(self):
        curr, start = None, None
        for index, block in enumerate(self.blocks):
            if curr != block:
                if curr is not None and start is not None:
                    yield File(curr, start, index - start)
                curr, start = block, index
        if curr is not None and start is not None:
            yield File(curr, start, len(self.blocks) - start)

    def defrag(self):
        for file in reversed(self.files()):
            pass

    def checksum(self):
        return sum(i * id for i, id in enumerate(self.blocks) if id is not None)


with open("test.txt") as fp:
    disk = Disk.parse(fp.read())
tree = FragmentationTree(disk.blocks, 0, 0)
print(tree)

print(disk)
pprint(list(disk.files()))