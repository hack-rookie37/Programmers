from itertools import combinations
from collections import defaultdict

def solution(orders, courses):
    answers = []

    for course in courses:
        course_dict = defaultdict(int)

        for order in orders:
            for comb in combinations(sorted(order), course):
                course_dict[''.join(comb)] += 1
        
        answer = []
        answer_cnt = 0

        for k, v in course_dict.items():
            if v == 1:
                continue

            if answer_cnt < v:
                answer = [k]
                answer_cnt = v
            elif answer_cnt == v:
                answer.append(k)

        answers.extend(answer)

    return sorted(answers)

# Test Case
test_cases = [  [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]], 
                [["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]],
                [["XYZ", "XWY", "WXA"], [2, 3, 4]]]
for test_case in test_cases:
    print(solution(*test_case))