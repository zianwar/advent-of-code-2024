from dataclasses import dataclass

with open("input.txt") as fp:
    data = fp.read()

@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y)


@dataclass
class Map:
    map: list[list[str]]

    @staticmethod
    def parse(data: str) -> 'Map':
        return Map([list(line) for line in data.splitlines()])
    
    def __repr__(self) -> str:
        return '\n'.join([''.join(line) for line in self.map])
    
    def __contains__(self, pos: Point) -> bool:
        return 0 <= pos.y < len(self.map) and 0 <= pos.x < len(self.map[0])

    def __getitem__(self, pos: Point):
        return self.map[pos.y][pos.x]
    
    def find(self, val:str) -> Point|None:
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == val:
                    return Point(x, y)

map = Map.parse(data)
guard = map.find('^')
DIRECTIONS = [Point(0, -1), Point(1, 0), Point(0, 1), Point(-1, 0)]
dir = 0

visited: set[Point] = set()
while guard in map:
    visited.add(guard)
    next = guard + DIRECTIONS[dir]
    if next in map and map[next] == "#":
        dir =  (dir + 1) % len(DIRECTIONS)
    else:
        guard = next

print(len(visited))




