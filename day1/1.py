with open("input.txt", "r") as fp:
    lines = fp.readlines()

left_list = []
right_list = []
for line in lines:
    left, right = line.split("   ")
    left_list.append(int(left))
    right_list.append(int(right))

left_list.sort()
right_list.sort()

total = sum([abs(x - y) for x, y in zip(left_list, right_list)])
print(total)
