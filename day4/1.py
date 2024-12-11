with open("input.txt") as fp:
    data = fp.read().splitlines()

DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def get_vector(start: tuple[int, int], direction: tuple[int, int]):
    return [
        (start[0] + direction[0] * i, start[1] + direction[1] * i) for i in range(4)
    ]


def get_word(data: list[str], vector: list[tuple[int, int]]):
    return "".join([data[v[0]][v[1]] for v in vector])


def get_words(data: list[str], start: tuple[int, int], width: int, height: int):
    for d in DIRECTIONS:
        vector = get_vector(start, d)
        if 0 <= vector[-1][0] < width and 0 <= vector[-1][1] < height:
            yield get_word(data, vector)


count = 0
h, w = len(data), len(data[0])
for x in range(w):
    for y in range(h):
        words = get_words(data, (x, y), w, h)
        for word in words:
            if word == "XMAS":
                count += 1
print(count)
