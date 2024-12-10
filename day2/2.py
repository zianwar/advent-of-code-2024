with open("input.txt", "r") as fp:
    lines = fp.read().splitlines()

reports = [[int(v) for v in line.split()] for line in lines]


def is_safe(report):
    diffs = [x - y for x, y in zip(report, report[1:])]
    return all(1 <= x <= 3 for x in diffs) or all(-3 <= x <= -1 for x in diffs)


count = 0
for report in reports:
    if any(is_safe(report[:i] + report[i + 1 :]) for i in range(len(report))):
        count += 1

print(count)
