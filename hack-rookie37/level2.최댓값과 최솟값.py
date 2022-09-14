def solution(s):
    x = list(map(int, s.split()))
    return " ".join([str(min(x)), str(max(x))])
