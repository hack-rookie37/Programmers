from collections import Counter


def solution(picks, minerals):

    plan = []
    for i in range(len(minerals) // 5 + 1):
        mins = Counter(minerals[i * 5 : (i + 1) * 5])
        plan.append((mins["diamond"], mins["iron"], mins["stone"]))

    plan = sorted(plan[: sum(picks)], reverse=True)
    L = len(plan)
    answer = 0
    i = 0
    wl = {0: [1, 1], 1: [5, 1], 2: [25, 5]}

    for p in range(3):
        while picks[p] > 0 and i < L:
            answer += plan[i][0] * wl[p][0] + plan[i][1] * wl[p][1] + plan[i][2]
            i += 1
            picks[p] -= 1

    return answer
