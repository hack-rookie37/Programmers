from collections import deque


p = {'[': ']', '{': '}', '(': ')'}

def check(s):
    t = list(s)
    i = 0
    
    while t:
        if t[i] in p.values():
            return False
        
        if len(t) <= 1:
            return False
        
        if p[t[i]] == t[i+1]:
            del t[i:i+2]
            i = 0
            continue
        i += 1
    
    return True
    

def solution(s):
    s = deque(s)
    answer = 0
    
    for _ in range(len(s)):
        if check(s):
            answer += 1
        s.rotate(-1)
        
    return answer