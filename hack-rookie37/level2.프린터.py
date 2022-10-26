from collections import deque


def solution(priorities, location):
    answer = 0

    q = deque(priorities)

    while q:
        if q[0] >= max(q):
            q.popleft()
            answer += 1
            if location == 0:
                break
            location -= 1

        else:
            q.append(q.popleft())
            if location == 0:
                location = len(q) - 1
            else:
                location -= 1

    return answer
