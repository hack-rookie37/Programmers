from collections import defaultdict, deque


def solution(topping):
    answer = 0

    r = defaultdict(deque)
    l = set()

    for i, t in enumerate(topping):
        r[t].append(i)

    for i, t in enumerate(topping):
        l.add(t)
        r[t].remove(i)

        if not r[t]:
            del r[t]

        if len(l) == len(r):
            answer += 1

        elif answer > 1:
            break

    return answer
