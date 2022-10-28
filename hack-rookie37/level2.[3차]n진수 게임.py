DIC = {k - 55: chr(k) for k in range(ord("A"), ord("F") + 1)}


def dec_to_n(x, n):
    ret = ""
    while x >= n:
        q, r = divmod(x, n)
        if r > 9:
            r = DIC[r]
        ret = str(r) + ret
        x = q

    if x > 9:
        ret = DIC[x] + ret
    else:
        ret = str(x) + ret

    return ret


def solution(n, t, m, p):
    last = m * t - (m - p)

    i = 0
    s = ""
    while len(s) < last:
        s += dec_to_n(i, n)
        i += 1

    answer = [s[it * m + p - 1] for it in range(t)]
    return "".join(answer)


solution(2, 4, 2, 1)
