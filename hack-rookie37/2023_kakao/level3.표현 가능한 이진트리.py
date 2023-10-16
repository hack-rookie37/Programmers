from math import log, ceil


def solution(numbers):
    answer = []

    def is_tree(bi, root_zero=False):
        len_bi = len(bi)
        if len_bi == 1:
            if root_zero and bi == '1':
                return False
            return True
        root = len_bi // 2

        if root_zero and bi[root] == '1':
            return False
        if bi[root] == '0':
            return is_tree(bi[:root], True) and is_tree(bi[root + 1:], True)
        else:
            return is_tree(bi[:root]) and is_tree(bi[root + 1:])

    for n in numbers:
        bi = bin(n)[2:]
        len_bi = len(bi)
        x = 2 ** ceil(log(len_bi + 1, 2)) - 1
        bi = '0' * (x - len_bi) + bi

        if is_tree(bi):
            answer.append(1)
        else:
            answer.append(0)

    return answer
