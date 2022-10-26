def solution(citations):

    c = sorted(citations, reverse=True)
    L = len(citations)

    for i in range(L - 1):
        for h in range(c[i], c[i + 1] - 1, -1):
            if h <= i + 1 and h >= L - i - 1:
                return h

    return min(c[-1], L)
