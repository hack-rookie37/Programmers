def solution(n, k):
    f = [0, 1]
    for i in range(2, n):
        f.append(f[-1] * i)

    answer = []
    cand = [i for i in range(1, n + 1)]
    x = k - 1
    while f[-1] != 0:
        Q, r = divmod(x, f[-1])
        answer.append(cand[Q])
        del cand[Q]
        f.pop()
        x = r

    return answer + cand
