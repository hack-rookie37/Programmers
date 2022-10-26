import re

p = re.compile("\d+(?:,\d+)*")


def solution(s):
    answer = []
    m = p.findall(s)
    d = dict()
    for x in m:
        x = x.split(",")
        d[len(x)] = set(map(int, x))

    answer.append(list(d[1])[0])
    for i in range(2, len(d) + 1):
        answer.append(list(d[i] - d[i - 1])[0])

    return answer
