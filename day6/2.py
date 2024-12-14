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

DIRECTIONS = [Point(0, -1), Point(1, 0), Point(0, 1), Point(-1, 0)]

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

    def __setitem__(self, pos: Point, val: str):
        self.map[pos.y][pos.x] = val
    
    def find(self, val:str) -> Point|None:
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == val:
                    return Point(x, y)
    
    def get_path(self, pos: Point):
        dir = 0
        path: set[Point] = set()
        while pos in map:
            path.add(pos)
            next = pos + DIRECTIONS[dir]
            if next in map and map[next] == "#":
                dir =  (dir + 1) % len(DIRECTIONS)
            else:
                pos = next
        return path

    def is_loop(self, pos: Point):
        DIRECTIONS = [Point(0, -1), Point(1, 0), Point(0, 1), Point(-1, 0)]
        dir = 0
        
        visited: set[tuple[Point, int]] = set()
        while pos in map:
            if (pos, dir) in visited:
                return True
            visited.add((pos, dir))
            
            next = pos + DIRECTIONS[dir]
            if next in map and map[next] == "#":
                dir =  (dir + 1) % len(DIRECTIONS)
            else:
                pos = next
        return False


map = Map.parse(data)
obstacle_count = 0
guard = map.find('^')
path = map.get_path(guard)
for p in path:
    map[p] = "#"
    if map.is_loop(guard):
        obstacle_count += 1
    map[p] = "."
print(obstacle_count)
