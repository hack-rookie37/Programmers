def solution(board, moves):
    N = len(board)
    answer = 0
    basket = [0]

    for m in moves:
        for i in range(N):
            if board[i][m - 1] != 0:
                if basket[-1] == board[i][m - 1]:
                    answer += 2
                    basket.pop()
                else:
                    basket.append(board[i][m - 1])
                board[i][m - 1] = 0
                break

    return answer
