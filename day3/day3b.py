import re

f = open("input")
raw = f.read()

matches = re.findall("(do\(\)|don't\(\))|mul\((\d+),(\d+)\)", raw)

total = 0
enabled = True
for (op, a, b) in matches:
    if op == "don't()":
        enabled = False
    elif op == 'do()':
        enabled = True
    elif enabled:
        total += int(a) * int(b)

print(total)
