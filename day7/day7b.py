import math

f = open("input")

def parse_line(line_str):
    test, numlist = line_str.split(": ")
    return int(test), [int(i) for i in numlist.split(' ')]

def solve(testval, equation):
    equation.reverse()
    return rec_solve(testval, equation.pop(), equation, [])

def rec_solve(testval, sum, equation, solution):
    if sum > testval:
        return False
    if len(equation) == 0:
        return sum == testval
    for operator in ['+', '*', '||']:
        eq = equation.copy()
        next = move(sum, eq, operator)
        if rec_solve(testval, next, eq, solution + [operator]):
            return True
    return False

def move(sum, equation, operator):
    next = equation.pop()
    if operator == '+':
        return sum + next
    elif operator == '*':
        return sum * next
    elif operator == '||':
        total = sum * (10 ** int(math.log10(next)+1)) + next
        return total

parsed = [parse_line(l) for l in f.read().split("\n")]

print(sum([testval for testval, equation in parsed if solve(testval, equation)]))