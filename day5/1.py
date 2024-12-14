with open("input.txt") as fp:
    rules, updates = fp.read().split("\n\n")

rules = [tuple(map(int, r.split("|"))) for r in rules.splitlines()]
updates = [list(map(int, u.split(","))) for u in updates.splitlines()]


def is_valid(update: list[str]) -> bool:
    update_idx = {n: idx for idx, n in enumerate(update)}
    for x, y in rules:
        if x not in update_idx or y not in update_idx:
            continue
        if update_idx[x] > update_idx[y]:
            return False
    return True


total = sum(
    [update[int(len(update) / 2)] if is_valid(update) else 0 for update in updates]
)
print(total)
