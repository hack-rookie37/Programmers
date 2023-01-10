from collections import deque


def solution(N, road, K):
    _map = [dict() for _ in range(N + 1)]

    for r in road:
        s, e, d = r
        if e in _map[s]:
            if d >= _map[s][e]:
                continue
        _map[s][e] = _map[e][s] = d

    q = deque([(1, 0)])
    visited = {1: 0}

    while q:
        node, d = q.popleft()
        for next_node in _map[node]:
            dist = _map[node][next_node]

            if next_node in visited:
                if visited[next_node] <= d + dist:
                    continue

            if d + dist <= K:
                visited[next_node] = d + dist
                q.append((next_node, d + dist))

    return len(visited)
