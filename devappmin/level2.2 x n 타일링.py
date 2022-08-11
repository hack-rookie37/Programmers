dvd = 1000000007

def solution(n):
    dp = [1, 2, 3]
    
    for idx in range(3, n):
        dp.append((dp[idx - 1] + dp[idx - 2]) % dvd)
    
    return dp[n - 1] % dvd

# Test Case
test_cases = [
                [4]
            ]
test_cases_answer = [5]
import time
for idx in range(len(test_cases)):
    s_time = time.process_time_ns()
    answer = 0
    answer = solution(*test_cases[idx])
    e_time = time.process_time_ns()
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS {}ms".format(( e_time - s_time ) / 1000000) if answer == test_cases_answer[idx] else "FAILED",end="\n\n")
