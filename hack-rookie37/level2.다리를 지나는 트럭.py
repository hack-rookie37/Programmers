from collections import deque


def solution(bl, w, tw):
    answer = 0
    bridge = deque([0] * bl)
    tw = deque(tw)
    count, C = 0, len(tw)

    while count < C:
        if bridge[0] != 0:
            w += bridge.popleft()
            count += 1
            bridge.append(0)

            if not tw or w < tw[0]:
                answer += 1

        while tw and tw[0] <= w:
            if bridge[-1] != 0 and bridge[0] == 0:
                bridge.append(bridge.popleft())
            elif bridge[-1] != 0 and bridge[-1] != 0:
                w += bridge.popleft()
                count += 1
                bridge.append(0)
            bridge[-1] = tw.popleft()
            w -= bridge[-1]
            answer += 1

        while count < C and bridge[0] == 0:
            bridge.append(bridge.popleft())
            answer += 1

    return answer
