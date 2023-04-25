def solution(k, ranges):
    answer = []
    k = float(k)

    hail = [k]
    while k != 1:
        if k % 2 == 0:
            k /= 2
            hail.append(k)
        else:
            k = k * 3 + 1
            hail.append(k)

    integral = []
    for i in range(len(hail) - 1):
        integral.append((hail[i] + hail[i + 1]) / 2)

    L = len(integral)

    for x, y in ranges:
        if x - y > L:
            answer.append(-1)
        elif y == 0:
            answer.append(sum(integral[x:]))
        else:
            answer.append(sum(integral[x:y]))

    return answer
