from __future__ import annotations

import os
from dataclasses import dataclass

os.system("clear")


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Point) -> Point:
        return Point(self.x - other.x, self.y - other.y)


DIRECTIONS = [Point(0, -1), Point(1, 0), Point(0, 1), Point(-1, 0)]


@dataclass
class Map:
    map: list[list[int]]

    @staticmethod
    def parse(data: str) -> Map:
        return Map([list(map(int, line)) for line in data.splitlines()])

    @property
    def width(self):
        return len(self.map[0])

    @property
    def height(self):
        return len(self.map)

    def __repr__(self) -> str:
        return "\n".join(["".join(line) for line in self.map])

    def __contains__(self, pos: Point) -> bool:
        return 0 <= pos.y < self.height and 0 <= pos.x < self.width

    def __getitem__(self, pos: Point):
        return self.map[pos.y][pos.x]

    def __setitem__(self, pos: Point, val: str):
        self.map[pos.y][pos.x] = val

    def get_trailheads(self) -> list[Point]:
        trailheads = []
        for x in range(self.width):
            for y in range(self.height):
                point = Point(x, y)
                if point in self and self[point] == 0:
                    trailheads.append(point)
        return trailheads


with open("input.txt") as fp:
    data = fp.read()

map = Map.parse(data)


def trails(pos: Point, start: Point, visited: set[tuple[Point, Point]]):
    if map[pos] == 9:
        visited.add((start, pos))

    for d in DIRECTIONS:
        next = pos + d
        if next in map and map[next] == map[pos] + 1:
            trails(next, start, visited)


trailheads = map.get_trailheads()
visited = set()
for t in trailheads:
    trails(t, t, visited)
print(len(visited))
