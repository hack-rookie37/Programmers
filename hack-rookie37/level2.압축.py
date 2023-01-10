def solution(msg):
    dic = {chr(k): k - 64 for k in range(ord("A"), ord("Z") + 1)}
    answer = []

    i, x = 0, 1
    L = len(msg)
    ni = 27

    while i < L:
        while msg[i : i + x] in dic and i + x <= L:
            x += 1
        answer.append(dic[msg[i : i + x - 1]])
        dic[msg[i : i + x]] = ni
        ni += 1
        i += x - 1
        x = 1

    return answer
