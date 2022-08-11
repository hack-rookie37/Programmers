def solution(numbers):
    return str(int(''.join(sorted(list(map(str, numbers)), key=lambda a: a * 3, reverse=True))))

# Test Case
test_cases = [
                [[6, 10, 2]],
                [[3, 30, 34, 5, 9]]
            ]
test_cases_answer = ["6210", "9534330"]
import time
for idx in range(len(test_cases)):
    s_time = time.process_time_ns()
    answer = 0
    answer = solution(*test_cases[idx])
    e_time = time.process_time_ns()
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS {}ms".format(( e_time - s_time ) / 1000000) if answer == test_cases_answer[idx] else "FAILED",end="\n\n")
