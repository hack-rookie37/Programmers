def solution(s):
    stack = []
    i = 0
    L = len(s)

    while i < L:
        while stack and i < L:
            if stack[-1] == s[i]:
                stack.pop()
                i += 1
            else:
                break

        if i < L:
            stack.append(s[i])
            i += 1

    return 0 if stack else 1
