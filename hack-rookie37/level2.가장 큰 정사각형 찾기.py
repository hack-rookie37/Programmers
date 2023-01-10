def solution(board):
    dxy = [(0, 1), (1, 0), (1, 1)]
    row = len(board)
    col = len(board[0])

    for x in range(row - 1, -1, -1):
        for y in range(col - 1, -1, -1):
            if board[x][y] == 0:
                continue
            adj = [1, 1, 1]
            for k in range(3):
                nx, ny = x + dxy[k][0], y + dxy[k][1]
                if not (0 <= nx < row and 0 <= ny < col):
                    break
                if board[nx][ny] == 0:
                    break
                adj[k] = board[nx][ny]
            else:
                board[x][y] = int((min(adj) ** 0.5 + 1) ** 2)

    return max(map(max, board))
