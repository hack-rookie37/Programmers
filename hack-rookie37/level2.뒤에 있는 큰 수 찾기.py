def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for i, n in enumerate(numbers):
        while stack:
            if stack[-1][1] < n:
                answer[stack[-1][0]] = n
                stack.pop()
            else:
                break

        stack.append((i, n))

    return answer


solution([2, 3, 3, 5])
