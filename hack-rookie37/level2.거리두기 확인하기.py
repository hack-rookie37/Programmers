from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(room, i, j, visit):
    d = 1
    queue = deque([(i, j, d)])
    visit[i][j] = True

    while queue:
        x, y, d = queue.popleft()
        if d > 2:
            break
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < len(room) and 0 <= ny < len(room) and not visit[nx][ny]:
                if room[nx][ny] == "P":
                    return False
                elif room[nx][ny] == "O":
                    queue.append((nx, ny, d + 1))
                    visit[nx][ny] = True
    return True


def check(room):
    visit = [[False] * 5 for _ in range(5)]
    for i, r in enumerate(room):
        for j, seat in enumerate(r):
            if seat == "P":
                if not bfs(room, i, j, visit):
                    return 0
    return 1


def solution(places):
    answer = []

    for room in places:
        answer.append(check(room))

    return answer
