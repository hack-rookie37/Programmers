from collections import deque


def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    s_q1 = sum(queue1)

    goal = (s_q1 + sum(queue2)) // 2
    cnt = 0

    while queue1 and queue2:
        if s_q1 == goal:
            return cnt
        elif s_q1 > goal:
            s_q1 -= queue1.popleft()
        else:
            queue1.append(queue2.popleft())
            s_q1 += queue1[-1]
        cnt += 1

    return -1
