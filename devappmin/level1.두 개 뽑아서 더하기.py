from itertools import combinations 

def solution(numbers):
    answer = []
    for num in combinations(numbers, 2):
        answer.append(sum(num))
    return sorted(set(answer))

# Test Case
test_cases = [
                [[2,1,3,4,1]],
                [[5,0,2,7]],
            ]
test_cases_answer = [[2,3,4,5,6,7], [2,5,7,9,12]]
import time
for idx in range(len(test_cases)):
    s_time = time.process_time_ns()
    answer = 0
    answer = solution(*test_cases[idx])
    e_time = time.process_time_ns()
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS {}ms".format(( e_time - s_time ) / 1000000) if answer == test_cases_answer[idx] else "FAILED",end="\n\n")
