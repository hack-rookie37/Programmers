def solution(gems):
    LEN = len(gems)
    KIND = len(set(gems))

    answer = []
    current = {gems[0]: 1}
    start, end = 0, 0

    while start < LEN:
        if len(current) < KIND:
            end += 1
            if end >= LEN:
                break
            current[gems[end]] = current.get(gems[end], 0) + 1
        else:
            if answer:
                if answer[2] > end - start:
                    answer = [start + 1, end + 1, end - start]
            else:
                answer = [start + 1, end + 1, end - start]

            current[gems[start]] -= 1
            if current[gems[start]] == 0:
                del current[gems[start]]
            start += 1

    return answer[:2]
