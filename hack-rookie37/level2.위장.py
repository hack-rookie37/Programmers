from collections import defaultdict
from itertools import combinations as cb
from functools import reduce


def solution(clothes):
    L = len(clothes)

    has = defaultdict(int)
    for _, body in clothes:
        has[body] += 1

    if len(has) == 30:
        return 2**30 - 1

    answer = L
    for i in range(2, L + 1):
        for comb in cb(has, i):
            m = 1
            for k in comb:
                m *= has[k]
            answer += m

    return answer
