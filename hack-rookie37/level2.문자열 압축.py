def solution(s):
    answer = float("inf")

    if len(s) == 1:
        return 1

    for i in range(1, len(s)):
        j = 0
        c = 1
        t = ""
        while j + i < len(s):
            if s[j : j + i] == s[j + i : j + i + i]:
                c += 1
            else:

                def make(c, t):
                    if c != 1:
                        t += str(c) + s[j : j + i]
                    else:
                        t += s[j : j + i]
                    return 1, t

                c, t = make(c, t)
            j += i

        c, t = make(c, t)
        answer = min(answer, len(t))

    return answer
