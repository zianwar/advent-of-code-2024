import itertools
import os
from dataclasses import dataclass
from pprint import pprint

os.system("clear")


@dataclass(frozen=True)
class Antenna:
    x: int
    y: int

    def __add__(self, other: "Antenna") -> "Antenna":
        return Antenna(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Antenna") -> "Antenna":
        return Antenna(self.x - other.x, self.y - other.y)


@dataclass
class Map:
    width: int
    height: int
    antennas: dict[str, set[Antenna]]

    @staticmethod
    def parse(s: str) -> "Map":
        antennas: dict[str, set[Antenna]] = {}
        lines = s.splitlines()
        for y, line in enumerate(lines):
            for x, label in enumerate(line):
                if label != ".":
                    if label not in antennas:
                        antennas[label] = set()
                    antennas[label].add(Antenna(x, y))
        return Map(len(lines[0]), len(lines), antennas)

    def find_antinodes(self):
        antinodes = set()
        for points in self.antennas.values():
            permutations = itertools.permutations(points, 2)
            for p1, p2 in permutations:
                diff = p2 - p1
                antinode = p2
                while 0 <= antinode.x < self.width and 0 <= antinode.y < self.height:
                    antinodes.add(antinode)
                    antinode += diff
        return antinodes


with open("input.txt") as fp:
    input = fp.read()

m = Map.parse(input)
antinodes = m.find_antinodes()
print(len(antinodes))
