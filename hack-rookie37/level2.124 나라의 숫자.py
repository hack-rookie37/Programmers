def solution(N):
    answer = []

    while N > 0:
        q, r = divmod(N, 3)

        if r == 1:
            answer.append("1")
        elif r == 2:
            answer.append("2")
        else:
            answer.append("4")
            q -= 1
        N = q

    return "".join(reversed(answer))
