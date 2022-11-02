def solution(dirs):
    answer = 0
    B = 11
    matrix = [[[0] * 4 for _ in range(B)] for _ in range(B)]
    cood = [5, 5]
    mv = {"U": (-1, 0, 0), "D": (1, 0, 1), "R": (0, 1, 2), "L": (0, -1, 3)}

    for d in dirs:
        x, y = cood
        nx, ny = x + mv[d][0], y + mv[d][1]

        if 0 <= nx < B and 0 <= ny < B:
            cood = [nx, ny]
            if matrix[x][y][mv[d][2]] == 0:
                answer += 1
                matrix[x][y][mv[d][2]] = 1

    return answer


# solution("ULURRDLLU")
solution("LULLLLLLU")
