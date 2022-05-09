import re
from itertools import permutations

def calculate(comb, expression):
    for char in comb:
        idx = 1

        while idx < len(expression) - 1:
            if expression[idx] == char:
                if char == '*':
                    expression[idx - 1] = int(expression.pop(idx - 1)) * int(expression.pop(idx))
                elif char == '+':
                    expression[idx - 1] = int(expression.pop(idx - 1)) + int(expression.pop(idx))
                elif char == '-':
                    expression[idx - 1] = int(expression.pop(idx - 1)) - int(expression.pop(idx))
            else:
                idx += 2

    return expression[0]

def solution(expression):
    expression = re.split(r'(\d*\.?\d+)', expression)[1:-1]
    ans = 0
    for comb in permutations(["*", "-", "+"], 3):
        ans = max(ans, abs(calculate(comb, [ *expression ])))

    return ans

# Test Case
test_cases =    [
                ["100-200*300-500+20"], 
                ["50*6-3*2"]
                ]
for test_case in test_cases:
    print(solution(*test_case))