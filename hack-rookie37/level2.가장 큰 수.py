from collections import defaultdict as d


def solution(numbers, x=0):

    if x >= 4:
        return "".join(map(str, numbers))

    hs = d(list)
    for num in numbers:
        s_num = str(num)
        while x >= len(s_num):
            s_num += s_num
        hs[s_num[x]].append(num)

    answer = ""
    for k in sorted(hs.keys(), reverse=True):
        if len(hs[k]) == 1:
            answer += str(hs[k][0])
        else:
            answer += solution(hs[k], x + 1)

    if x == 0 and int(answer) == 0:
        return "0"
    return answer


def e_solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int("".join(numbers)))
