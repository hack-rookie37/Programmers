def solution(sequence, k):
    last = len(sequence) - 1
    answer = [0, last]
    s = e = 0

    x = sequence[0]
    while s <= last and e <= last:
        if x == k:
            if (answer[-1] - answer[0]) > e - s:
                answer = [s, e]

            elif (answer[-1] - answer[0]) == e - s:
                if s < answer[0]:
                    answer = [s, e]
            x -= sequence[s]
            s += 1
        elif x > k:
            x -= sequence[s]
            s += 1

        else:
            e += 1
            if e <= last:
                x += sequence[e]

    return answer
