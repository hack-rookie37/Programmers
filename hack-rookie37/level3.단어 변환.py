from collections import deque


def solution(begin, target, words):
    LEN = len(begin)

    answer = 0
    visited = set()
    dist = 0
    q = deque([(begin, dist)])

    while q:
        w, dist = q.popleft()
        if w == target:
            answer = dist
            break
        for word in words:
            count = 0
            for c in range(LEN):
                if w[c] != word[c]:
                    count += 1
            if count > 1:
                continue
            if word not in visited:
                q.append((word, dist + 1))
                visited.add(word)

    return answer
