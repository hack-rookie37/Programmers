from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = set()
    q = deque()

    for c in cities:
        c = c.upper()
        if c in cache:
            q.remove(c)
            q.append(c)
            answer += 1
        else:
            if len(q) < cacheSize:
                q.append(c)
                cache.add(c)
            elif cache:
                cache.remove(q.popleft())
                q.append(c)
                cache.add(c)
            answer += 5

    return answer


solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
