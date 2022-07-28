from collections import deque

d = [1, -1]


def solution(numbers, target):
    answer = 0
    q = deque([(0, 0)])
    L = len(numbers)

    while q:
        x, n = q.popleft()

        if n == L and x == target:
            answer += 1

        if n < L:
            for k in range(2):
                nx = x + numbers[n] * d[k]
                q.append((nx, n + 1))

    return answer
