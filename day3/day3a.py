import re

f = open("input")
raw = f.read()

matches = re.findall("mul\((\d+),(\d+)\)", raw)

result = sum([int(a) * int(b) for (a, b) in matches])

print(result)
