def solution(brown, yellow):
    m = []
    for i in range(1, yellow // 2 + 1):
        if yellow % i == 0:
            m.append(i)

    m.append(yellow)

    answer = []
    for h in m:
        w = yellow // h + 2
        if (2 * w) + (2 * h) == brown:
            answer.append(w)
            answer.append(h + 2)
            break

    return answer
