def solution(numbers):
    answer = []

    for n in numbers:
        bn = "0" + format(n, "b")
        ret = list(bn)
        index = None
        L = len(ret)

        for i in range(L - 1, -1, -1):
            if bn[i] == "0":
                ret[i] = "1"
                index = i
                break

        if index == L - 1:
            answer.append(int("".join(ret), 2))
        else:
            ret[index + 1] = "0"
            answer.append(int("".join(ret), 2))

    return answer
