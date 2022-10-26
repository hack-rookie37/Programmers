from collections import defaultdict

Q = 65536


def solution(str1, str2):

    str1, str2 = str1.upper(), str2.upper()
    d1, d2 = defaultdict(int), defaultdict(int)

    for s in range(len(str1) - 1):
        if str1[s].isalpha() and str1[s + 1].isalpha():
            d1[str1[s] + str1[s + 1]] += 1
    for s in range(len(str2) - 1):
        if str2[s].isalpha() and str2[s + 1].isalpha():
            d2[str2[s] + str2[s + 1]] += 1

    i_set = d1.keys() & d2.keys()
    u_set = d1.keys() | d2.keys()

    if not u_set:
        return Q

    x = y = 0
    for i in i_set:
        x += min(d1[i], d2[i])
    for u in u_set:
        y += max(d1[u], d2[u])

    return int(x / y * Q)
