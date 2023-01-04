def solution(n):
    answer = [[0] * (i + 1) for i in range(n)]
    S = (n * (n + 1)) // 2
    dxy = {0: (1, 0), 1: (0, 1), 2: (-1, -1)}

    x, y, d = 0, 0, 0
    for i in range(1, S + 1):
        dx, dy = dxy[d % 3]
        nx, ny = x + dx, y + dy

        if not (0 <= nx < n and 0 <= ny < n) or answer[nx][ny]:
            nx, ny = nx - dx, ny - dy
            d += 1
            dx, dy = dxy[d % 3]
            nx, ny = nx + dx, ny + dy

        answer[x][y] = i
        x, y = nx, ny

    return [a for sublist in answer for a in sublist]
