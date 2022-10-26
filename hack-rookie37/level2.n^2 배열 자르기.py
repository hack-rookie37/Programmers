def solution(n, left, right):

    L = tuple(map(lambda x: x + 1, divmod(left, n)))
    R = tuple(map(lambda x: x + 1, divmod(right, n)))

    if L[0] == R[0]:
        return [i if i > L[0] else L[0] for i in range(L[1], R[1] + 1)]

    L_side = [i if i > L[0] else L[0] for i in range(L[1], n + 1)]
    R_side = [j if j > R[0] else R[0] for j in range(1, R[1] + 1)]

    if R[0] - L[0] < 2:
        return L_side + R_side

    for i in range(L[0] + 1, R[0]):
        for j in range(1, n + 1):
            L_side += [j if j > i else i]

    return L_side + R_side


solution(3, 2, 5)
