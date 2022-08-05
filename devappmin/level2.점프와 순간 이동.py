# https://velog.velcdn.com/images%2Fju_h2%2Fpost%2F1bcbcb7c-28c9-44ec-96a5-f36cdd88b4a3%2FKakaoTalk_20201210_122904168.jpg

def solution(n):
    return bin(n).count('1')

# Test Case
test_cases = [
                [5],
                [6],
                [5000]
            ]
test_cases_answer = [2, 2, 5]
import time
for idx in range(len(test_cases)):
    s_time = time.process_time_ns()
    answer = 0
    answer = solution(*test_cases[idx])
    e_time = time.process_time_ns()
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS {}ms".format(( e_time - s_time ) / 1000000) if answer == test_cases_answer[idx] else "FAILED",end="\n\n")
