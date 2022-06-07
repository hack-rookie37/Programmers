def move(matrix, x1, y1, x2, y2):
    mini = temp = matrix[x1][y1]

    # up
    for i in range(x1 + 1, x2 + 1):
        matrix[i - 1][y1] = matrix[i][y1]
        if mini > matrix[i][y1]:
            mini = matrix[i][y1]

    # left
    for j in range(y1 + 1, y2 + 1):
        matrix[x2][j - 1] = matrix[x2][j]
        if mini > matrix[x2][j]:
            mini = matrix[x2][j]
    # down
    for i in range(x2 - 1, x1 - 1, -1):
        matrix[i + 1][y2] = matrix[i][y2]
        if mini > matrix[i][y2]:
            mini = matrix[i][y2]

    # right
    for j in range(y2 - 1, y1 - 1, -1):
        matrix[x1][j + 1] = matrix[x1][j]
        if mini > matrix[x1][j]:
            mini = matrix[x1][j]

    matrix[x1][y1 + 1] = temp

    return mini


def solution(rows, columns, queries):
    matrix = [
        [(r - 1) * columns + c for c in range(1, columns + 1)]
        for r in range(1, rows + 1)
    ]

    answer = []

    for q in queries:
        answer.append(move(matrix, *map(lambda x: x - 1, q)))

    return answer
