def solution(cards):
    answer = [0, 0]
    n = k = len(cards)
    total = k * (k + 1) // 2
    cards = [0] + cards

    box = 1
    while total and k > answer[0]:
        cnt = 0
        while cards[box]:
            nxt = cards[box]
            cards[box] = 0
            total -= nxt
            cnt += 1
            box = nxt

        if cnt > answer[1]:
            answer[0] = answer[1]
            answer[1] = cnt
        elif cnt > answer[0]:
            answer[0] = cnt

        for b in range(2, n + 1):
            if cards[b]:
                box = b
                break

        k -= cnt

    return answer[0] * answer[1]
