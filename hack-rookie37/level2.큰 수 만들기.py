def solution(number, k):
    answer = ""

    L = len(number)
    M = max(number)
    start = 0
    end = k
    while start < L and end < L:
        t_max = "0"
        for j in range(start, end + 1):
            if t_max < number[j]:
                start = j + 1
                t_max = number[j]
                if t_max == M:
                    break
        answer += t_max
        end += 1

    return answer
