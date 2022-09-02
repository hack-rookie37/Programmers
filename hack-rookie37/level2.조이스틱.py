from collections import deque


def move(change, n, idx=0, dist=0):
    global x

    if len(change) <= 0:
        x = min(x, dist)
        return

    for i in (0, -1):
        gap = min(abs(idx - change[i]), n - abs(idx - change[i]))
        if i == 0:
            move(change[1:], n, change[i], dist + gap)
        else:
            move(change[:-1], n, change[i], dist + gap)


def solution(name):
    global x
    answer = 0

    for c in name:
        asc = ord(c)
        if 65 <= asc <= 78:
            answer += asc - 65
        else:
            answer += 91 - asc

    change = [i for i, c in enumerate(name) if c != "A" and i != 0]

    x = float("inf")
    move(change, len(name))

    return x + answer
