from functools import reduce


def solution(data, col, row_begin, row_end):
    answer = []
    data = sorted(data, key=lambda x: (x[col - 1], -x[0]))
    mod = lambda x: x % (s + 1)
    for s in range(row_begin - 1, row_end):
        answer.append(sum(map(mod, data[s])))

    return reduce(lambda x, y: x ^ y, answer)
