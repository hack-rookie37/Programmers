from itertools import permutations as pm


def solution(k, dungeons):
    answer = 0
    L = len(dungeons)

    for case in pm(dungeons, L):
        tk = k
        exp = 0
        for d in case:
            if tk >= d[0]:
                exp += 1
                tk -= d[1]
        answer = max(answer, exp)
        if answer == L:
            return answer

    return answer
