from collections import deque 

def is_balanced(p):
    s = deque()
    
    for char in p:
        s.append(char)
        
        while len(s) >= 2 and s[-1] == ')' and s[-2] == '(':
            s.pop()
            s.pop()
    
    return False if s else True
    

def subsolution(s):
    if len(s) == 0: return ''

    cursor, pos = 0, 0
    for char in s:
        pos += 1
        
        if char == '(':
            cursor += 1
        else:
            cursor -= 1
            
        if cursor == 0:
            break
        
    
    if is_balanced(s[:pos]):
        return s[:pos] + subsolution(s[pos:])
    else:
        return '(' + subsolution(s[pos:]) + ')' + ''.join(['(' if x == ')' else ')' for x in s[1:pos - 1]])
        
def solution(p):
    return subsolution(p)

# Test Case
test_cases = [
                ["(()())()"], 
                [")("],
                ["()))((()"]
            ]
test_cases_answer = ["(()())()", "()", "()(())()"]
for idx in range(len(test_cases)):
    answer = solution(*test_cases[idx])
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS" if answer == test_cases_answer[idx] else "FAILED {}".format(idx),end="\n\n")