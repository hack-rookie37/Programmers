answer = 0


def solution(n):
    global answer
    cood_y = [0] * n

    def n_queen(x, y):
        global answer
        cood_y[x] = y

        for iy in range(x, -1, -1):
            for biy in range(iy - 1, -1, -1):
                if cood_y[iy] == cood_y[biy] or abs(iy - biy) == abs(
                    cood_y[iy] - cood_y[biy]
                ):
                    return

        if x >= n - 1:
            # print(cood_y)
            answer += 1
            return

        for y in range(n):
            n_queen(x + 1, y)

    if n % 2 == 0:
        for y in range(n // 2):
            n_queen(0, y)
        answer *= 2
    else:
        for y in range(n // 2):
            n_queen(0, y)
        t_answer = answer * 2
        answer = 0
        n_queen(0, n // 2)
        answer += t_answer

    return answer
