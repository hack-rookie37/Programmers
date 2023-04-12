from collections import deque


def solution(maps):
    answer = []

    dx = (1, -1, 0, 0)
    dy = (0, 0, 1, -1)

    maps = [list(x) for x in maps]

    row = len(maps)
    col = len(maps[0])

    for i in range(row):
        for j in range(col):
            if maps[i][j] == "X":
                continue
            island = 0
            q = deque([(i, j)])

            while q:
                x, y = q.popleft()
                if maps[x][y] == "X":
                    continue

                island += int(maps[x][y])
                maps[x][y] = "X"
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < row and 0 <= ny < col and maps[nx][ny] != "X":
                        q.append((nx, ny))

            answer.append(island)

    return sorted(answer) if answer else [-1]
