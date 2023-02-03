BLOCK = 10000000


def real_solution(begin, end):
    answer = [1] * (end - begin + 1) if begin != 1 else [0] + [1] * (end - begin)

    for i in range(begin, end + 1):
        k, cap = 2, int(i ** (1 / 2))
        while k <= cap:
            Q, r = divmod(i, k)
            if r == 0 and Q <= BLOCK:
                answer[i - begin] = Q
                break
            k += 1

        if answer[i - begin] == 1:
            for x in range(cap - 1, 1, -1):
                if i % x == 0:
                    answer[i - begin] = x
                    break

    return answer


def solution(begin, end):
    answer = [1] * (end - begin + 1) if begin != 1 else [0] + [1] * (end - begin)

    for i in range(begin, end + 1):
        k, cap = 2, int(i ** (1 / 2))
        while k <= cap:
            Q, r = divmod(i, k)
            if r == 0 and Q <= BLOCK:
                answer[i - begin] = Q
                break
            k += 1

    return answer
