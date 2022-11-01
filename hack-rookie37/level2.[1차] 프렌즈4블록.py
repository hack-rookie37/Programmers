def solution(m, n, board):
    dxy = [(1, 0), (1, 1), (0, 1)]
    board = list(map(list, board))


    def explore(board, x, y):
        start = board[x][y]
        if start == "x":
            return False, 0

        for k in range(3):
            nx, ny = x + dxy[k][0], y + dxy[k][1]
            if 0 <= nx < m and 0 <= ny < n:
                if board[nx][ny] != start:
                    return False, k
            else:
                return False, k

        return True, None


    def move(board):
        new_board = [
            [board[x][y] for x in range(m) if board[x][y] != "x"] for y in range(n)
        ]

        for y in range(n):
            L = len(new_board[y])
            if L < m:
                new_board[y] = ["x"] * (m - L) + new_board[y]

        return [[new_board[y][x] for y in range(n)] for x in range(m)]


    answer = 0
    while True:
        bang = set()
        i = j = 0
        while i < m and j < n:
            boom, k = explore(board, i, j)
            if boom:
                bang.add((i, j))
                bang.add((i + 1, j))
                bang.add((i + 1, j + 1))
                bang.add((i, j + 1))
                j += 1
            else:
                if k == 0 or k == 1:
                    j += 1
                else:
                    j += 2

            if j >= n:
                i += 1
                j = 0
        for i, j in bang:
            board[i][j] = "x"

        L = len(bang)
        if L == 0:
            break

        answer += L
        board = move(board)

    return answer
    