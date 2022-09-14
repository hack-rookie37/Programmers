import math 


def solution(w, h):
    return w * h - (w + h - math.gcd(w, h))

# 전체 넓이에서 선이 지나가지 않은 부분을 없애서 선이 지나는 곳을 구할 수 있다.
# 선이 지나가지 않는 부분은 가로와 세로를 합한 뒤에 가로와 세로의 최대공약수를 빼는 것으로 문제를 해결할 수 있다.

# Test Case
test_cases = [[8, 12]]
test_cases_answer = [80]
import time
for idx in range(len(test_cases)):
    s_time = time.process_time_ns()
    answer = solution(*test_cases[idx])
    e_time = time.process_time_ns()
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS {}ms".format(( e_time - s_time ) / 1000000) if answer == test_cases_answer[idx] else "FAILED",end="\n\n")
