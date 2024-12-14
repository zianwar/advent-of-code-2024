with open("input.txt") as fp:
    rules, updates = fp.read().split("\n\n")

rules = [tuple(map(int, r.split("|"))) for r in rules.splitlines()]
updates = [list(map(int, u.split(","))) for u in updates.splitlines()]

#TODO