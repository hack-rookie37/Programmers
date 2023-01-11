def solution(order):
    stack = []

    n = len(order)

    box, o = 1, 0
    answer = 0
    while order and o < n:
        if box == order[o]:
            answer += 1
            o += 1
            box += 1

        elif stack:
            if stack[-1] == order[o]:
                stack.pop()
                answer += 1
                o += 1
            elif stack[-1] < order[o]:
                stack.append(box)
                box += 1
            else:
                break

        else:
            stack.append(box)
            box += 1

    return answer
