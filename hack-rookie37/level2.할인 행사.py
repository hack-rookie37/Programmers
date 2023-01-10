from collections import defaultdict, Counter


def solution(want, number, discount):
    answer = 0
    to_buy = dict((k, v) for k, v in zip(want, number))

    sale = defaultdict(int)
    for d in discount[:10]:
        sale[d] += 1

    lack = set()
    for prod in to_buy:
        if to_buy[prod] > sale[prod]:
            lack.add(prod)

    if not lack:
        answer += 1

    loop_cnt = len(discount) - 10
    for l in range(loop_cnt):
        new, old = discount[l + 10], discount[l]
        sale[old] -= 1
        sale[new] += 1

        if old in to_buy:
            if sale[old] < to_buy[old]:
                lack.add(old)

        if new in to_buy:
            if sale[new] == to_buy[new]:
                if new in lack:
                    lack.remove(new)

        if not lack:
            answer += 1

    return answer
