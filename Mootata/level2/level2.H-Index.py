def solution(citations):
    l = len(citations)
    for idx, h in enumerate(sorted(citations)):
        diff = l - idx
        if h >= diff:
            return diff
    return 0

print(solution([10, 10, 10, 10, 10]))