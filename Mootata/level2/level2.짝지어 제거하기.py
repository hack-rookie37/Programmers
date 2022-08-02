def solution(s):
    string = list(s)
    stack = []
    stack.append(string[0])
    
    for i in string[1:]:
        stack.append(i)
        
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    
    if stack:
        return 0
    else:
        return 1

print(solution("baabaa"))