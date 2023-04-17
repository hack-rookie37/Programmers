from collections import defaultdict


def solution(weights):
    answer = 0
    pair = defaultdict(int)

    for w in weights:
        answer += pair[w]
        answer += pair[w * 2 / 3] + pair[w * 3 / 2]
        answer += pair[w * 3 / 4] + pair[w * 4 / 3]
        answer += pair[w * 4 / 2] + pair[w * 2 / 4]
        pair[w] += 1

    return answer
