from dataclasses import dataclass


@dataclass
class Disk:
    blocks: list[int | None]

    @staticmethod
    def parse(data: str) -> "Disk":
        blocks: list[int | None] = []
        for i, size in enumerate(data):
            blocks += [i // 2 if i % 2 == 0 else None] * int(size)
        return Disk(blocks)

    def defrag(self):
        l, r = 0, len(self.blocks) - 1

        while l < r:
            if self.blocks[l] is not None:
                l += 1
            elif self.blocks[r] is None:
                r -= 1
            else:
                self.blocks[l], self.blocks[r] = self.blocks[r], None

    def checksum(self):
        return sum(i * id for i, id in enumerate(self.blocks) if id is not None)


with open("input.txt") as fp:
    disk = Disk.parse(fp.read())
disk.defrag()
print(disk.checksum())
