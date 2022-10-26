from collections import defaultdict
from itertools import combinations as cb


def solution(orders, course):
    answer = []

    d = defaultdict(int)

    for c in course:
        for order in orders:
            for menu in cb(sorted(order), c):
                d[menu] += 1

    for c in course:
        t = []
        for key in d:
            if len(key) == c and d[key] > 1:
                if t:
                    if t[-1][1] < d[key]:
                        t = [(key, d[key])]
                    elif t[-1][1] == d[key]:
                        t.append((key, d[key]))
                else:
                    t.append((key, d[key]))

        for s in t:
            answer.append("".join(s[0]))

    return sorted(answer)
