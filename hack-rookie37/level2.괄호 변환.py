def check(u):
    l = r = 0
    for x in u:
        if r > l:
            return False
        if x == "(":
            l += 1
        elif x == ")":
            r += 1
    return True


def solution(p):
    answer = ""

    if not p:
        return p

    l = r = 0
    for x in p:
        if l != 0 and l == r:
            break
        if x == "(":
            l += 1
        elif x == ")":
            r += 1

    u, v = p[: l + r], p[l + r :]
    if check(u):
        answer = u + solution(v)
    else:
        answer = "(" + solution(v) + ")"
        for x in range(1, len(u) - 1):
            if u[x] == "(":
                answer += ")"
            else:
                answer += "("

    return answer


solution("()))((()")
