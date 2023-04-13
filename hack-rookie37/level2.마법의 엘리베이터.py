def solution(storey):
    answer = 0
    x = storey
    i = 1
    while x > 0:
        move = round(x, -i)
        c = 10**i
        if x % c == 5 * c:
            if int(str(move)[0]) < 5:
                move = (x // c) * c
        answer += abs(x - move) // 10 ** (i - 1)
        x = move
        i += 1
    return answer
