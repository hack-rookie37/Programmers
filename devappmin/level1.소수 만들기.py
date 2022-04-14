from itertools import combinations

def solution(nums):
    answer = 0
    for items in combinations(nums, 3):
        m_sum = sum(items)
        m_bool = True
        
        for di in range(2, m_sum//2):
            if not m_sum % di:
                m_bool = False
        
        if m_bool:
            answer += 1
        
    return answer

# Test Case
test_cases = [[[1, 2, 3, 4]], [[ 1, 2, 7, 6, 4 ]]]
for test_case in test_cases:
    print(solution(*test_case))