from collections import defaultdict


def solution(today, terms, privacies):
    answer = []
    t = defaultdict(int)

    y, m, d = map(lambda x: int(x), today.split('.'))
    for term in terms:
        name, date = term.split()
        t[name] = int(date)

    for i, p in enumerate(privacies):
        pdate, pterm = p.split()
        py, pm, pd = map(lambda x: int(x), pdate.split('.'))

        pm += t[pterm]
        if pm > 12:
            q, r = divmod(pm, 12)
            if r:
                py += q
                pm = r
            else:
                py += q - 1
                pm = 12

        pd -= 1

        if pd == 0:
            pm -= 1
            pd = 28
            if pm <= 0:
                py -= 1
                pm = 12

        if py > y:
            continue
        elif py < y:
            answer.append(i + 1)
            continue
        else:
            if pm > m:
                continue
            elif pm < m:
                answer.append(i + 1)
                continue
            elif pd < d:
                answer.append(i + 1)

    return answer
