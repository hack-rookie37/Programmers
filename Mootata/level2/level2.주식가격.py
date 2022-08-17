def solution(prices):
    answer = [i for i in range(len(prices) - 1, -1, -1)]
    stack = []
    
    for idx, p in enumerate(prices):
        while stack and prices[stack[-1]] > p:
            pre = stack.pop()
            answer[pre] = idx - pre
        stack.append(idx)
    return answer

print(solution([1, 2, 3, 2, 3, 1, 1]))