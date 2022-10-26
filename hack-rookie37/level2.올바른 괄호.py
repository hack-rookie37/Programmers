def solution(s):
    o = c = 0

    for i in s:
        if o < c:
            break
        if i == "(":
            o += 1
        else:
            c += 1
    else:
        if o == c:
            return True
        else:
            False

    return False
