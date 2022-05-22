from collections import deque

def solution(st):
    s = deque()
    
    for char in st:
        s.append(char)
        
        while len(s) >= 2 and s[-1] == s[-2]:
            s.pop()
            s.pop()
    
    return 1 if not s else 0

# Test Case
test_cases = [
                ["baabaa"], 
                ["cdcd"],
            ]
test_cases_answer = [1, 0]
for idx in range(len(test_cases)):
    answer = solution(*test_cases[idx])
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS" if answer == test_cases_answer[idx] else "FAILED {}".format(idx),end="\n\n")