from itertools import combinations


def sub_solution(answer, cols):
    for cand in answer:
        if set(cand).issubset(set(cols)):
            return True
    return False


def solution(relation):
    L_row, L_col = len(relation), len(relation[0])
    answer = []

    for i in range(1, L_col+1):
        for cols in combinations(range(L_col), i):

            if sub_solution(answer, cols):
                continue

            distinct = []
            for r in range(L_row):
                row = []
                for c in cols:
                    row.append(relation[r][c])
                distinct.append(tuple(row))
            if len(distinct) == len(set(distinct)):
                answer.append(cols)

    return len(answer)
