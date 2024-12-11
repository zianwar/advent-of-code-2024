with open("input.txt") as fp:
    data = fp.read().splitlines()

count = 0
h, w = len(data), len(data[0])
for x in range(w):
    for y in range(h):
        is_valid = 0 < x < w - 1 and 0 < y < h - 1
        if data[x][y] == "A" and is_valid:
            top_left = data[x - 1][y - 1]
            top_right = data[x - 1][y + 1]
            bottom_left = data[x + 1][y - 1]
            bottom_right = data[x + 1][y + 1]

            # check for
            # M.S      S.M      M.M      S.S
            # .A.  or  .A.  or  .A.  or  .A.
            # M.S      S.M      S.S      M.M
            # or

            if (
                (
                    top_left == "M"
                    and top_right == "S"
                    and bottom_left == "M"
                    and bottom_right == "S"
                )
                or (
                    top_left == "S"
                    and top_right == "M"
                    and bottom_left == "S"
                    and bottom_right == "M"
                )
                or (
                    top_left == "M"
                    and top_right == "M"
                    and bottom_left == "S"
                    and bottom_right == "S"
                )
                or (
                    top_left == "S"
                    and top_right == "S"
                    and bottom_left == "M"
                    and bottom_right == "M"
                )
            ):
                count += 1

print(count)
