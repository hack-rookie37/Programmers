dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
direction = {"S": [0, 1, 2, 3], "L": [2, 3, 1, 0], "R": [3, 2, 0, 1]}


def check(nx, ny, row, col):
    if nx >= row:
        nx = 0
    elif nx < 0:
        nx = row - 1
    if ny >= col:
        ny = 0
    elif ny < 0:
        ny = col - 1

    return nx, ny


def solution(grid):
    answer = []
    row, col = len(grid), len(grid[0])
    matrix = [[[0] * 4 for _ in range(col)] for _ in range(row)]

    for r in range(row):
        for c in range(col):
            for k in range(4):
                if matrix[r][c][k] != 0:
                    continue
                matrix[r][c][k] = 1
                nx, ny = check(r + dx[k], c + dy[k], row, col)
                count, d = 1, k

                while True:
                    x, y, d = nx, ny, direction[grid[nx][ny]][d]
                    nx, ny = check(nx + dx[d], ny + dy[d], row, col)
                    if matrix[x][y][d] != 0:
                        break
                    matrix[x][y][d] = 1
                    count += 1

                answer.append(count)

    return sorted(answer)
