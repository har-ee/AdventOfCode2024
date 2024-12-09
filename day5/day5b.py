f = open("input")

raw_rules, raw_update = f.read().split("\n\n")
rules = [[int(l) for l in r.split("|")] for r in raw_rules.strip().split("\n")]
update = [[int(l) for l in u.split(",")] for u in raw_update.strip().split("\n")]

before_to_after = dict()
after_to_before = dict()

for [before, after] in rules:
    if before not in before_to_after:
        before_to_after[before] = set()
    if after not in after_to_before:
        after_to_before[after] = set()
    before_to_after[before].add(after)
    after_to_before[after].add(before)

def in_order(b_to_a, a_to_b, updates):
    for i, cur in enumerate(updates):
        before = set(updates[:i])
        after = set(updates[i+1:])
        if cur in a_to_b:
            intersect = a_to_b[cur].intersection(after)
            if len(intersect) > 0:
                return False, i, intersect
        if cur in b_to_a:
            intersect = b_to_a[cur].intersection(before)
            if len(intersect) > 0:
                return False, i, intersect
    return True, None, set()

def iter_swap(b_to_a, a_to_b, updates):
    while True:
        ordered, elem, conflicts = in_order(b_to_a, a_to_b, updates)
        if ordered:
            return updates
        first_conflict = updates.index(conflicts.pop())
        updates[elem], updates[first_conflict] =  updates[first_conflict], updates[elem]

def mid(updates):
    return updates[int(len(updates)/2)]

print(sum([mid(iter_swap(before_to_after, after_to_before, u)) for u in update if not in_order(before_to_after, after_to_before, u)[0]]))