# 카카오 2018 신입공채 3차 코딩테스트 5번 문제

di = [-1, 1]


def solution(words):
    answer = 0

    words.sort()
    L = len(words)

    for i in range(len(words)):
        count = 0
        for k in range(2):
            ni = i + di[k]
            if 0 <= ni < L:
                R = min(len(words[i]), len(words[ni]))
                t = 0
                for c in range(R):
                    t += 1
                    if words[i][c] != words[ni][c]:
                        break
                else:
                    if len(words[i]) > len(words[ni]):
                        t += 1
                count = max(count, t)
        answer += count

    return answer
