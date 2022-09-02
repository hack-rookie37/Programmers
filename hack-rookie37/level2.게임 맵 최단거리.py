from collections import deque


def solution(maps):

    q = deque([(0, 0, 1)])
    N, M = len(maps), len(maps[0])
    visited = set()

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    while q:
        x, y, dist = q.popleft()

        if x == N - 1 and y == M - 1:
            return dist

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if maps[nx][ny] != 0 and (nx, ny) not in visited:
                    q.append((nx, ny, dist + 1))
                    visited.add((nx, ny))

    return -1
