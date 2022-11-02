def solution(elements):
    answer = set()

    e = elements * 2

    for i in range(len(elements)):
        j = i + 1
        while j - i <= len(elements):
            answer.add(sum(e[i:j]))
            j += 1

    return len(answer)
