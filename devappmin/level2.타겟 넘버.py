answer = 0

def dfs(val, idx, length, numbers, target):
    if idx == length:
        if val == target:
            global answer
            answer += 1
        
        return 
    
    dfs(val - numbers[idx], idx + 1, length, numbers, target)
    dfs(val + numbers[idx], idx + 1, length, numbers, target)

def solution(numbers, target):
    dfs(0, 0, len(numbers), numbers, target)
    return answer

# Test Case
test_cases = [[[ 1, 1, 1, 1, 1 ], 3], [[4, 1, 2, 1], 4]]
for test_case in test_cases:
    print(solution(*test_case))
    answer = 0
