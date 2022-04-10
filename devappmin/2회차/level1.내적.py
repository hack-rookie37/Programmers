def solution(a, b):
    return sum([a[x] * b[x] for x in range(len(a))])

# Test Case
test_cases = [[[1, 2, 3, 4], [-3, -1, 0, 2]], [[ -1, 0, 1 ], [1, 0, -1]]]
for test_case in test_cases:
    print(solution(*test_case))