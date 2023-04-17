from collections import deque


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ROW, COL = 0, 0


def bfs(m, start, goal):
    cnt, end = 0, None
    q = deque([start + [0]])
    while q:
        x, y, cnt = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < ROW and 0 <= ny < COL:
                if m[nx][ny] != "X":
                    if m[nx][ny] == goal:
                        return cnt + 1, [nx, ny]
                    q.append((nx, ny, cnt + 1))
                    m[nx][ny] = "X"
    return cnt, end


def solution(maps):
    global ROW, COL
    ROW, COL = len(maps), len(maps[0])

    answer = 0
    start = [0, 0]
    for r in range(ROW):
        for c in range(COL):
            if maps[r][c] == "S":
                start = [r, c]
                break

    phase = ["L", "E"]
    for p in phase:
        cnt, start = bfs(list(map(list, maps)), start, p)
        if start:
            answer += cnt
        else:
            return -1

    return answer
