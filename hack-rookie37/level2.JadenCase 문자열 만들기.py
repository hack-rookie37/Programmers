def solution(s):

    answer = ""
    first = True

    for c in s:
        t = c
        if first:
            if isinstance(c, str):
                t = c.upper()
        else:
            if isinstance(c, str):
                t = c.lower()

        answer += t
        if c == " ":
            first = True
        else:
            first = False

    return answer
