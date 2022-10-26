from collections import defaultdict
import time


def solution(X, Y):
    xd = defaultdict(int)
    yd = defaultdict(int)

    for x in X:
        xd[x] += 1

    for y in Y:
        yd[y] += 1

    answer = ""

    for n in range(9, -1, -1):
        s = str(n)
        if s in xd and s in yd:
            answer += s * min(xd[s], yd[s])

    if answer:
        print("yes")

    if not answer:
        return "-1"

    elif int(answer) == 0:
        return "0"

    else:
        return answer


N = 1000000
print(solution("011" * N, "110" * N))
