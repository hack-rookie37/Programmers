def solution(n, words):
    answer = [0, 0]
    once = set()

    for i, w in enumerate(words):
        order, man = divmod(i, n)

        if w in once:
            answer[0], answer[1] = man + 1, order + 1
            break

        if i >= 1:
            if words[i - 1][-1] != w[0]:
                answer[0], answer[1] = man + 1, order + 1
                break

        once.add(w)

    return answer
