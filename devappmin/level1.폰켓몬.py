def solution(nums):
    return min(len(nums) // 2, len(set(nums)))

# Test Case
test_cases = [
    [[3,1,2,3]],
    [[3,3,3,2,2,4]],
    [[3,3,3,2,2,2]]
]
test_cases_answer = [2, 3, 2]
import time
for idx in range(len(test_cases)):
    s_time = time.process_time_ns()
    answer = 0
    answer = solution(*test_cases[idx])
    e_time = time.process_time_ns()
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS {}ms".format(( e_time - s_time ) / 1000000) if answer == test_cases_answer[idx] else "FAILED",end="\n\n")
