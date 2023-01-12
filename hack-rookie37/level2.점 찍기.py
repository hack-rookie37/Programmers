import math


def solution(k, d):
    answer = 0
    for y in range(0, d + 1, k):
        max_x = (d**2 - y**2) ** 0.5
        answer += math.ceil(max_x / k) + (1 if max_x % k == 0 else 0)

    return answer
