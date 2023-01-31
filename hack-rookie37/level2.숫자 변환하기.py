from collections import deque


def solution(x, y, n):
    answer = -1

    q = deque([(x, 0)])
    v = set()

    while q:
        x, k = q.popleft()

        if x == y:
            answer = k
            break

        if x <= y * 3 and x * 3 not in v:
            q.append((x * 3, k + 1))
            v.add(x * 3)

        if x <= y * 2 and x * 2 not in v:
            q.append((x * 2, k + 1))
            v.add(x * 2)

        if x <= y + n and x + n not in v:
            q.append((x + n, k + 1))
            v.add(x + n)

    return answer
