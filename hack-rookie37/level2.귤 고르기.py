from collections import defaultdict


def solution(k, tang):
    answer = set()

    kind = defaultdict(int)
    for t in tang:
        kind[t] += 1

    kind = [(k, kind[k]) for k in kind]
    kind.sort(key=lambda x: x[1], reverse=True)

    i = 0
    L = len(tang)
    while k > 0 and i < L:
        answer.add(kind[i][0])
        k -= kind[i][1]
        i += 1

    return len(answer)
