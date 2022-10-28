def solution(prices):
    L = len(prices)
    stack = []
    answer = [0]*L
    
    for i, p in enumerate(prices):
        if stack:
            while stack[-1][0] > p:
                dp, di = stack[-1]
                answer[di] = i-di
                stack.pop()
                
        stack.append((p,i))
    
    for i, a in enumerate(answer):
        if a == 0:
            answer[i] = L-i-1
        
    for i, a in enumerate(answer):
        if a == 0:
            answer[i] = L-i-1

    # list comprehension
    # answer = [L-i-1 if a == 0 else a for i, a in enumerate(answer)]
    
    return answer


print(solution([1,2,3,2,3]))