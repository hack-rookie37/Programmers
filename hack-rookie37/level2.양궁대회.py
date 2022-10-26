from itertools import combinations


def solution(n, info):
    gap = sum([i - 10 for i in range(11) if info[i] != 0])
    answer = [[0]*11, gap]

    for case in combinations(range(11), n):
        t_n = n
        t_answer = [0]*11
        t_gap = gap

        for i in case:
            if info[i] == 0:
                t_answer[i] = 1
                t_n -= 1
                t_gap += 10 - i
            else:
                if t_n > info[i]:
                    t_answer[i] = info[i] + 1
                    t_n -= info[i] + 1
                    t_gap += (10 - i) * 2
            if t_n < 1:
                break

        if t_gap > answer[1]:
            if t_n > 0:
                t_answer[-1] = t_n
            answer[0] = t_answer
            answer[1] = t_gap
        elif t_gap == answer[1]:
            for i in range(11):
                x = sum(answer[0][10-i:-1])
                y = sum(t_answer[10-i:-1])
                if x < y:
                    answer[0] = t_answer
                    answer[1] = t_gap
                    break
                elif x > y:
                    break

    return answer[0] if answer[1] > 0 else [-1]
