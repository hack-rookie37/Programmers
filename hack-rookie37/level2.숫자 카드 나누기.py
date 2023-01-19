def solution(A, B):
    def find_a(x, y, min_x):
        cd = []
        for i in range(1, int(min_x**0.5) + 1):
            q, r = divmod(min_x, i)
            if r == 0:
                cd.append(i)
                cd.append(q)

        cd = sorted(cd, reverse=True)
        for q in cd:
            if all(e % q == 0 for e in x) and all(e % q != 0 for e in y):
                return q

        return 0

    return max(find_a(A, B, min(A)), find_a(B, A, min(B)))
