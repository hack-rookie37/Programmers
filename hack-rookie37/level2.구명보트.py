from collections import deque


def solution(people, limit):
    q = deque(sorted(people))

    answer = 0
    while q:
        x = limit

        while q and x >= q[-1]:
            x -= q.pop()

        while q and x >= q[0]:
            x -= q.popleft()

        answer += 1

    return answer
