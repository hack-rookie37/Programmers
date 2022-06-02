from collections import defaultdict

def solution(gems):
    left, right = 0, 0
    various = len(list(set(gems)))
    contains = defaultdict(int)
    contains[gems[0]] += 1
    answer = []
    n = 1
    
    if various == 1:
        return [1, 1]
    
    while left <= right:
        if contains[gems[left]] >= 2:
            contains[gems[left]] -= 1
            left += 1
            
        elif right == len(gems) - 1:
            contains[gems[left]] -= 1
            if contains[gems[left]] == 0:
                n -= 1
            left += 1
            
        else:
            right += 1
            contains[gems[right]] += 1
            if contains[gems[right]] == 1:
                n += 1
        
        if various == n:
            answer.append([left + 1, right + 1])
            
    return sorted(answer, key=lambda a: a[1] - a[0])[0]

# Test Case
test_cases = [
                [["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]],
                [["AA", "AB", "AC", "AA", "AC"]],
                [["XYZ", "XYZ", "XYZ"]],
                [["ZZZ", "YYY", "NNNN", "YYY", "BBB"]],
            ]
test_cases_answer = [[3, 7], [1, 3], [1, 1], [1, 5]]
import time
for idx in range(len(test_cases)):
    s_time = time.process_time_ns()
    answer = solution(*test_cases[idx])
    e_time = time.process_time_ns()
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS {}ms".format(( e_time - s_time ) / 1000000) if answer == test_cases_answer[idx] else "FAILED",end="\n\n")